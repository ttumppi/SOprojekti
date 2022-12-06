from django.shortcuts import render, redirect
from .forms import BoardgamerForm
from .forms import PasswordsForm
from .forms import Login_Form
from .models import Boardgamer
from .models import Passwords
from .forms import BoardgameForm
from datetime import datetime
#from .models import User_Info

from .models import Boardgame
def homepage(request):
    if 'user' in request.session:
        if authentication(request.session.get('user')) == False:
            user = False
            dict = {'user':user}
            return render(request, "board_games/homepage.html", dict)
        boardgamer = Boardgamer.objects.get(id=request.session['user'])
        user = True
        dict = {'user':user, 'boardgamer':boardgamer}
        return render(request, "board_games/homepage.html", dict)
    return render(request, "board_games/homepage.html")

#List of all boardgames
def boardgames(request):
    if 'user' in request.session:
        if authentication(request.session.get('user')) == False:
            return redirect('board_games:error')
    boardgame = Boardgame.objects.all()
    dict = user_object(request.session.get('user'))
    boardgamer = dict.get('user_object')
    user = dict.get('user')
    dict = {'boardgames':boardgame, 'user':user, 'boardgamer':boardgamer}
    return render(request, "board_games/boardgames.html", dict)

def boardgame(request, boardgame_id):
    if 'user' in request.session:
        if authentication(request.session.get('user')) == False:
            return redirect('board_games:error')
    """Show a single boardgame and its details"""
    is_loaned = False
    boardgame = Boardgame.objects.get(id=boardgame_id)
    if request.method == 'POST':
        if 'user' in request.session:
            boardgamer = Boardgamer.objects.get(id = request.session['user'])
            if boardgame.boardgamer == boardgamer:
                return redirect('board_games:error')
            #print (boardgamer.varaukset)
            #boardgamer.varaukset = 0
            if boardgamer.varaukset == 3:
                return redirect('board_games:error')
            boardgame.boardgamer = boardgamer
            boardgamer.varaukset +=1
            boardgame.loan_date = datetime.now()
            boardgamer.save()
            boardgame.save()
            is_loaned = True
            dict = user_object(request.session.get('user'))
            boardgamer = dict.get('user_object')
            user = dict.get('user')
            dict = {'boardgame_id':boardgame_id, 'boardgame':boardgame, 'is_loaned':is_loaned, 'boardgamer':boardgamer, 'user':user}
            return render(request, 'board_games/boardgame.html', dict)
        else:
            return redirect('board_games:error')

    if boardgame.boardgamer != None and request.session['edited'] == False:
        gamer = Boardgamer.objects.get(id=boardgame.boardgamer.id)
        is_loaned = True
        dict = user_object(request.session.get('user'))
        boardgamer = dict.get('user_object')
        user = dict.get('user')
        dict = {'boardgame_id':boardgame_id, 'boardgame':boardgame, 'is_loaned':is_loaned, 'gamer':gamer, 'boardgamer':boardgamer, 'user':user}
        return render(request, 'board_games/boardgame.html', dict)

    if request.session['edited'] == True:
        request.session['edited'] = False
        boardgame.edit_date = datetime.now()
        boardgame.save()
        is_loaned = False
        dict = user_object(request.session.get('user'))
        boardgamer = dict.get('user_object')
        user = dict.get('user')
        dict = {"True":True, 'boardgame':boardgame, 'is_loaned':is_loaned, 'boardgamer':boardgamer, 'user':user}
        return render(request, "board_games/boardgame.html", dict)
    dict = user_object(request.session.get('user'))
    boardgamer = dict.get('user_object')
    user = dict.get('user')
    dict = {'boardgame':boardgame, 'user':user, 'boardgamer':boardgamer, 'is_loaned':is_loaned}
    return render(request, 'board_games/boardgame.html', dict)

def register(request):
    if request.method == 'POST':
        form = BoardgamerForm(request.POST)
        form_password = PasswordsForm(request.POST)
        if form.is_valid() and form_password.is_valid():
            form_object = form.save(commit=False)
            #nimen katsaus tietokantaan
            for i in Boardgamer.objects.all():
                if form_object.nimi == i.nimi:
                    return redirect('board_games:error')
            form_password_object = form_password.save(commit=False)
            Passwords.hash(form_password_object,form_object)
            #form_password_object.username = form_object
            #form_object.save()
            #form_password_object.save()
            return redirect('board_games:homepage')
    form = BoardgamerForm()
    form_password = PasswordsForm()
    dict = {'form':form, 'form_password':form_password}

    return render(request, 'board_games/register.html', dict)

def log_in(request):
    if request.method == 'POST':
        form = Login_Form(request.POST)

        if form.is_valid():
            for user in Boardgamer.objects.all():
                if form.cleaned_data['username'] == user.nimi:
                    #Boardgamer objektiin linkittyvä password objekti haku
                    password_object = Passwords.objects.get(username_id=user.id)
                    #Tällä hetkellä loopissa olevan Boardgamer objektin id valinta
                    if Passwords.hash_check(form.cleaned_data['password'], user) == True:

                    #if form.cleaned_data['password'] == password_object.salasana:
                        request.session['user'] = user.id
                        request.session['edited'] = False
                        #return render(request, 'board_games/succesful.html')
                        return redirect('board_games:homepage')  
                    
            return redirect('board_games:error')
    else:
        form = Login_Form()
        dict = {'form':form}
    return render(request, 'board_games/log_in.html', dict)

def error(request):
    return render(request, 'board_games/error.html')



def log_out(request):
    if 'user' in request.session:
        if authentication(request.session.get('user')) == False:
            return redirect('board_games:error')
    #user = User_Info.objects.get(username_id = User_Info.gamer_id)
    #user.delete()
    request.session['user'] = False
    return render(request, 'board_games/log_out.html')

def loans(request):
    if 'user' in request.session:
        if authentication(request.session.get('user')) == False:
            return redirect('board_games:error')
    if 'user' in request.session:
        pelaaja = Boardgamer.objects.get(id=request.session['user'])
        pelit = pelaaja.boardgame_set.all()
        dict = user_object(request.session.get('user'))
        boardgamer = dict.get('user_object')
        user = dict.get('user')
        dict = {'pelit':pelit, 'boardgamer':boardgamer, 'user':user}
        return render(request, "board_games/loans.html", dict)
    return redirect('board_games:error')

def returning(request, game_id):
    peli = Boardgame.objects.get(id=game_id)
    peli.boardgamer = None
    peli.save()
    user = Boardgamer.objects.get(id=request.session['user'])
    user.varaukset -=1
    user.save()
    return redirect('board_games:loans')

def new_boardgame(request):
    if 'user' in request.session:
        if authentication(request.session.get('user')) == False:
            return redirect('board_games:error')
    if 'user' not in request.session:
        return redirect('board_games:error')
    if request.method != 'POST':
        form = BoardgameForm()
    else:
        form = BoardgameForm(data=request.POST)
        if form.is_valid():       
            boardgame = form.save(commit=False)
            for i in Boardgamer.objects.all():
                print (i.id, request.session.get('user'))
                if request.session['user'] == i.id:
                    boardgame.owner = i
                    boardgame.edit_date = datetime.now()
                    boardgame.loan_date = datetime.now()
                    boardgame.save()
                    return redirect('board_games:boardgames')
    dict = user_object(request.session.get('user'))
    boardgamer = dict.get('user_object')
    user = dict.get('user')                
    context = {'form': form, 'boardgamer':boardgamer, 'user':user}
    return render(request, 'board_games/new_boardgame.html', context)

def edit_boardgame(request, boardgame_id):
    if 'user' in request.session:
        if authentication(request.session.get('user')) == False:
            return redirect('board_games:error')
    boardgame = Boardgame.objects.get(id=boardgame_id)
    
    if request.method == 'POST':
        form = BoardgameForm(request.POST)
        if form.is_valid:
            form_object = form.save(commit=False)
            boardgame.nimi = form_object.nimi
            boardgame.selitys = form_object.selitys
            boardgame.save()
            request.session['edited'] = True
            return redirect('board_games:boardgame', boardgame_id)
    else:
        form = BoardgameForm()
        dict = user_object(request.session.get('user'))
        boardgamer = dict.get('user_object')
        user = dict.get('user')
        dict = {'boardgame':boardgame, 'boardgame_id':boardgame_id, 'form':form, 'boardgamer':boardgamer, 'user':user}
        return render(request, "board_games/edit_boardgame.html", dict)

def delete_boardgame(request, boardgame_id):
    if 'user' in request.session:
        if authentication(request.session.get('user')) == False:
            return redirect('board_games:error')
    boardgame = Boardgame.objects.get(id= boardgame_id)
    boardgame.delete()
    return redirect("board_games:boardgames")

def authentication(session):
    for i in Boardgamer.objects.all():
        if i.id == session:
            return True 
    return False
def user_object(user_id):
    for i in Boardgamer.objects.all():
        if i.id == user_id:
            dict = {'user_object':i, 'user':True}
            return dict
def created_games(request, gamer_id):
     if 'user' in request.session:
        if authentication(request.session.get('user')) == False:
            return redirect('board_games:error')
        else:
            boardgames = []
            gamer = Boardgamer.objects.get(id=gamer_id)
            for i in Boardgame.objects.all():
                if i.owner == gamer:
                    boardgames.append(i)
            dict = user_object(request.session.get('user'))
            boardgamer = dict.get('user_object')
            user = dict.get('user')
            dict = {'boardgames':boardgames, 'boardgamer':boardgamer, 'user':user}
            return render(request, "board_games/created_games.html", dict)



