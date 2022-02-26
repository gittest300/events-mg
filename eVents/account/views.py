from tkinter import N
from tkinter.messagebox import NO
from unicodedata import category
from django.shortcuts import render
from .works_biz import EventBL
from django.core.paginator import Paginator
from datetime import datetime
# Create your views here.
start_date = None
end_date = None
category = None
keywords = None

def homeView(request):
    res = {}
    global start_date 
    global end_date 
    global category 
    global keywords
    start_date = None
    end_date = None
    category = None
    keywords = None
    try:
        event_list = EventBL().get_events()[:3]
        res['event_list'] = event_list
    except Exception as err:
        res = {'error': err}
    finally:
        return render(request, 'index.html', res)

def eventsView(request, type=0):
    res = {}
    try:
        global start_date 
        global end_date 
        global category 
        global keywords
        data_res = []
        categories = EventBL().get_categories()
        event_list = EventBL().get_events()
        if event_list:
            pass
        if request.method=="POST":
            start_date = request.POST.get('start_date', None)
            end_date = request.POST.get('end_date', None)
            category = request.POST.get('category', None)
            keywords = request.POST.get('keyword', None)
        if end_date:
            event_list = event_list.filter(start_date__date__lte=end_date)
            res['end_date'] = end_date
        if start_date:
            event_list = event_list.filter(start_date__date__gte=start_date)
            res['start_date'] = start_date
        if category not in (0, '0', None):
            res['category'] = {'category_id': category, 'category_name': categories.get(category_id=category)}
            categories = categories.exclude(category_id=category)
            event_list = event_list.filter(category__category_id=category)
        if keywords:
            res['end_date'] = end_date
            event_list = event_list.filter(title__icontains=keywords)

        page_number = request.GET.get('page')
        paginator = Paginator(event_list, 10) # Show 10 contacts per page.
        page_obj = paginator.get_page(page_number)
        res['categories'] = categories
        res['event_list'] = page_obj
    except Exception as err:
        print(err)
        res = {'error': err}
    finally:
        return render(request, 'events.html', res)

def eventsListView(request):
    return eventsView(request, type=1)
