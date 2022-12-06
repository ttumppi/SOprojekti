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
    path('returning/<int:game_id>/', views.returning, name='returning'),
    path('new_boardgame/,´', views.new_boardgame, name='new_boardgame'),
    path('edit_boardgame/<int:boardgame_id>/', views.edit_boardgame, name='edit_boardgame'),
    path('delete_boardgame/<int:boardgame_id>/', views.delete_boardgame, name='delete_boardgame'),
    path('created_games/<int:gamer_id>/', views.created_games, name='created_games'),
]