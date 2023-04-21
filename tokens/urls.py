from django.urls import path
from . import views

urlpatterns = [
    path('add_play_tokens/', views.add_play_tokens_page, name='add_play_tokens_page'),
    path('add_play_tokens/add/', views.add_play_tokens, name='add_play_tokens'),
    path('viewall/', views.account_balances),
]
