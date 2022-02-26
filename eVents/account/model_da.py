from .models import EventModel
from .models import Categories

class EventDA():
    def __init__(self):
        pass

    def get_all_events(self):
        return EventModel.objects.all()
    
    def get_all_published_events(self):
        return EventModel.objects.filter(published = True)

    def get_all_paid_events(self):
        return EventModel.objects.filter(is_paid = True)

    def get_all_categories(self):
        return Categories.objects.all()