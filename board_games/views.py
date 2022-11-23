from django.shortcuts import render

from .models import Boardgame
def homepage(request):
    return render(request, "board_games/homepage.html")

#List of all boardgames
def boardgames(request):
    boardgame = Boardgame.objects.all()
    dict = {'boardgames':boardgame}
    return render(request, "board_games/boardgames.html", dict)