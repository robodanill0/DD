from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bug_reports_url = reverse('quality_control:bug_list')
    feature_request_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_reports_url}'><h2>Список всех багов</a></h2><h2><a href='{feature_request_url}'>Запросы на улучшение</a></h2>"
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse("Список всех багов.")

def feature_list(request):
    return HttpResponse("Запросы на улучшение.")