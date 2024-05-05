from django.http import HttpResponse
from django.urls import reverse
from quality_control.urls import *

def index(request):
    another_page_url = reverse('tasks:another_page')
    html = f"<h1>Страница приложения tasks</h1><h2><a href='{another_page_url}'></h2><h2>Перейти на другую страницу</a></h2><h2><a href='/quality_control/'>Перейти на quality_control</a></h2>"
    return HttpResponse(html)

def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")