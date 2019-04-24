from django.urls import path

from . import views

urlpatterns = [
    # ex: /capture/
    path('', views.index, name='index'),
    # ex: /capture/5/
    path('<int:capture_id>/', views.detail, name='detail'),
    # ex: /capture/all
    path('all/', views.all, name='all'),
]

