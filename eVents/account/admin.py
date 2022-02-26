from django.contrib import admin
from .models import EventModel
from .models import Categories
from .models import LikedModel
# Register your models here.
admin.site.register(EventModel)
admin.site.register(Categories)
admin.site.register(LikedModel)