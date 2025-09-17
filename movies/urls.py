from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='movies.index'),
    path('hidden', views.hidden, name='movies.hidden'),
    path('hide/<int:id>/', views.hide, name='movies.hide'),
    path('unhide/<int:id>/', views.unhide, name='movies.unhide'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='movies.delete_review'),
]
