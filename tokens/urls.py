from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_play_tokens/', views.add_play_tokens_page, name='add_play_tokens_page'),
    path('add_play_tokens/add/', views.add_play_tokens, name='add_play_tokens'),
    path('add_gift_tokens/', views.add_gift_tokens_page, name='add_gift_tokens_page'),
    path('add_gift_tokens/add/', views.add_gift_tokens, name='add_gift_tokens'),
    path('reset/', views.reset_accounts, name='reset_accounts'),
    path('viewall/', views.account_balances),
]
