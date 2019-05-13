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
    # ex; /capture/undelete/5
    path('undelete/<int:capture_id>', views.undelete, name='undelete'),
    # ex; /capture/logbook
    path('capture/logbook', views.logbook, name='logbook'),
    # ex; /capture/log_item/5
    path('capture/log_item/<int:capture_id>', views.log_item, name='log_item'),
    # ex; /capture/today
    path('capture/today', views.today, name='today'),
    # ex; /capture/calendar
    path('capture/calendar', views.calendar, name='calendar'),
    # ex; /capture/anytime
    path('capture/anytime', views.anytime, name='anytime'),
    # ex; /capture/projects
    path('capture/projects', views.projects, name='projects'),
]

