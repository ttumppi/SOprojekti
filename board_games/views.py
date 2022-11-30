from django.shortcuts import render, redirect
from .forms import BoardgamerForm
from .forms import PasswordsForm
from .forms import Login_Form
from django.forms.formsets import formset_factory
from .models import Boardgamer
from .models import Passwords
#from .models import User_Info

from .models import Boardgame
def homepage(request):
    return render(request, "board_games/homepage.html")

#List of all boardgames
def boardgames(request):
    boardgame = Boardgame.objects.all()
    dict = {'boardgames':boardgame}
    return render(request, "board_games/boardgames.html", dict)

def boardgame(request, boardgame_id):
    """Show a single boardgame and its details"""
    boardgame = Boardgame.objects.get(id=boardgame_id)
    dict = {'boardgame_id':boardgame_id, 'boardgame':boardgame}
    if request.method == 'POST':
        if 'user' in request.session:
            boardgamer = Boardgamer.objects.get(id = request.session['user'])
            if boardgame.boardgamer == boardgamer:
                return redirect('board_games:error')
            boardgame.boardgamer = boardgamer
            boardgamer.varaukset =+1
            boardgamer.save()
            boardgame.save()
            return render(request, 'board_games/boardgame.html', dict)
        else:
            return redirect('board_games:error')

    return render(request, 'board_games/boardgame.html', dict)

def register(request):
    if request.method == 'POST':
        form = BoardgamerForm(request.POST)
        form_password = PasswordsForm(request.POST)

        if form.is_valid() and form_password.is_valid():
            form_object = form.save(commit=False)
            form_password_object = form_password.save(commit=False)
            form_password_object.username = form_object
            form_object.save()
            form_password_object.save()
            return redirect('board_games:homepage')
    else:
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
                    if form.cleaned_data['password'] == password_object.salasana:
                        request.session['user'] = user.id
                        return render(request, 'board_games/succesful.html')  
            return redirect('board_games:error')
    else:
        form = Login_Form()
        dict = {'form':form}
    return render(request, 'board_games/log_in.html', dict)

def error(request):
    return render(request, 'board_games/error.html')

# def succesful(request):
#     user_object = request.session['user']
#     user = Boardgamer.objects.get(id=user_object)
#     username = User_Info()
#     username.username = user.nimi
#     username.gamer_id = request.user.id
#     username.save()
#     dict = {'nimi':user.nimi}
#     return render(request, 'board_games/succesful.html', dict)

def log_out(request):
    #user = User_Info.objects.get(username_id = User_Info.gamer_id)
    #user.delete()
    request.session.flush()
    return render(request, 'board_games/log_out.html')

def loans(request):
    if 'user' in request.session:


        pelaaja = Boardgamer.objects.get(id=request.session['user'])
        pelit = pelaaja.boardgame_set.all()
        print (pelit)
        dict = {'pelit':pelit}
        return render(request, "board_games/loans.html", dict)
    return redirect('board_games:error')
