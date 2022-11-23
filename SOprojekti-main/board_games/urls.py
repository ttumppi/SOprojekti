from django.urls import path

from .import views

app_name = 'board_games'
urlpatterns = [
    #home page
    path('', views.homepage, name='homepage'),
    path('boardgames', views.boardgames, name='boardgames')
]