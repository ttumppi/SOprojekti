from django.urls import path

from .import views

app_name = 'board_games'
urlpatterns = [
    #home page
    path('', views.homepage, name='homepage'),
    path('boardgames', views.boardgames, name='boardgames'),
    # Detail page for a single boardgame
    path('boardgames/<int:boardgame_id>/', views.boardgame, name='boardgame'),
    path('register/', views.register, name='register'),
    path('log_in/', views.log_in, name='log_in'),
    path('error/', views.error, name='error'),
    #path('succesful/', views.succesful, name='succesful'),
    path('log_out/', views.log_out, name='log_out'),
    path('loans/', views.loans, name='loans'),
]