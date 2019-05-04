from django.urls import path

from . import views

app_name = 'capture'
urlpatterns = [
    # ex: /capture/
    path('', views.index, name='index'),
    # ex: /capture/5/
    path('<int:capture_id>/', views.detail, name='detail'),
    # ex: /capture/all
    path('all/', views.all, name='all'),
    # ex: /capture/capture
    path('capture/', views.capture, name='capture'),
    # ex: /capture/bin
    path('capture/bin', views.paper_bin, name='paper_bin'),
    # ex; /capture/delete/5
    path('delete/<int:capture_id>', views.delete, name='delete'),
]

