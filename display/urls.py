from django.urls import path
from . import views

urlpatterns = [
    path ('',views.index),
    path('shows', views.all_shows),
    path('shows/new', views.new_show),
    path('process_new_show', views.process_new_show),
    path('<int:val>/edit', views.edit),
    path('shows/<int:val>', views.show),
    path('<int:val>/delete', views.delete)
    
]
