from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from .models import BugReport, FeatureRequest
from django.views.generic import DetailView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_reports_url = reverse('quality_control:bug_list')
        feature_request_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1><a href='{bug_reports_url}'><h2>Список всех багов</a></h2><h2><a href='{feature_request_url}'>Запросы на улучшение</a></h2>"
        return HttpResponse(html)
    
def index(request):
    bug_reports_url = reverse('quality_control:bug_list')
    feature_request_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_reports_url}'><h2>Список всех багов</a></h2><h2><a href='{feature_request_url}'>Запросы на улучшение</a></h2>"
    return HttpResponse(html)

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список всех BugReport</h1><ul>'
    for bug in bugs:
        bug_detail_url = reverse('quality_control:bug_detail', kwargs={'bug_id': bug.id})
        bugs_html += f'<li><a href="{bug_detail_url}">{bug.title}</a><br>Status: {bug.status}<br></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'
        response_html += f'<li>Status: {bug.status}</li><li>Priority: {bug.priority}</li>'
        response_html += f'<li>Task\'s name: <b>{bug.task.name}</b></li><li>Project\'s name: <b>{bug.project.name}</li>' # Без переадресации оставлю имя
        response_html += '</ul>'
        return HttpResponse(response_html)
    
class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature_request = self.object
        response_html = f'<h1>{feature_request.title}</h1><p>{feature_request.description}</p>'
        response_html += f'<li>Status: {feature_request.status}</li><li>Priority: {feature_request.priority}</li>'
        response_html += f'<li>Task\'s name: <b>{feature_request.task.name}</b></li><li>Project\'s name: <b>{feature_request.project.name}</li>' # Без переадресации оставлю имя
        response_html += '</ul>'
        return HttpResponse(response_html)
    
def bug_detail(request, bug_id):
    return HttpResponse("Детали бага " + str(bug_id))

def feature_id_detail(request, feature_id):
    return HttpResponse("Детали улучшения " + str(feature_id))

def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список всех FeatureRequest</h1><ul>'
    for feature in features:
        feature_detail_url = reverse('quality_control:feature_id_detail', kwargs={'feature_id': feature.id})
        features_html += f'<li><a href="{feature_detail_url}">{feature.title}</a><br>Status: {feature.status}<br></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)
