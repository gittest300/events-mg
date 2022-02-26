from .models import EventModel
from .models import Categories
from .model_da import EventDA

class EventBL():
    def __init__(self):
        pass
    def get_events(self):
        return EventDA().get_all_events().order_by('start_date')
    def get_categories(self):
        return EventDA().get_all_categories()
    