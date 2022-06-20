from django.urls import path
from . import views #same directory as urls

urlpatterns = [ 
    path('', views.flashcards, name = 'flashcards'), 
    path(r'create/', views.create_card_set, name = 'create_card_set'), 
    path(r'create_card/(?P<card_set_id>[\d]+)', views.create_card, name = 'create_card'), 
    path(r'delete/(?P<card_set_id>[\d]+)', views.delete_card_set, name = 'delete_card_set'), 
    path(r'delete_card/(?P<card_id>[\d]+)', views.delete_card, name = 'delete_card'), 
    path(r'edit/(?P<card_set_id>[\d]+)', views.edit_card_set, name = 'edit_card_set'),
    path(r'edit_card/(?P<card_id>[\d]+)', views.edit_card, name = 'edit_card'), 
    path(r'view/(?P<card_set_id>[\d]+)', views.view_card_set, name = 'view_card_set'), 
    path(r'dictionary/', views.dictionary, name = 'dictionary'),
]