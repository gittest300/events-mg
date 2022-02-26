from django.urls import path,include
from .views import homeView
from .views import eventsView
from .views import eventsListView

urlpatterns = [
    path('', homeView, name='home'),
    path('events', eventsView, name='events'),
    path('events-list', eventsListView, name='events_list'),
] 
