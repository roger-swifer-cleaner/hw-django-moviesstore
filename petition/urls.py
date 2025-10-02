from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='petition.index'),
    path('vote/<int:id>', views.vote, name='petition.vote'),
    path('unvote/<int:id>', views.unvote, name='petition.unvote'),
    path('delete/<int:id>', views.delete_petition, name='petition.delete'),
    path('create', views.make_petition, name='petition.make_petition'),
]
