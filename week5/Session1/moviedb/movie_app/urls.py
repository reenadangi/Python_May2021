from django.urls import path,include
from  . import views
urlpatterns = [
    path('',views.index),
    path('directors',views.directors),
    path('directors/<int:id>',views.show_director),
    path('directors/create',views.create_director),
    path('directors/<int:id>/destroy',views.destroy_director),
    
    path('movies',views.movies),
    path('movies/create',views.create_movie),
    path('movies/<int:id>',views.show_movie),
    path('movies/<int:id>/edit',views.edit_movie),
    path('movies/<int:id>/update',views.update_movie),
    path('movies/<int:id>/destroy',views.destroy_movie),
    
    path('actors',views.actors),
    path('actors/create',views.create_actor),
    path('movies/<int:id>/add_actor',views.add_actor),
   
]


