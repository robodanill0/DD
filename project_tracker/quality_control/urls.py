from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'), 
	path('bug_detail/<int:bug_id>', views.bug_detail, name='bug_detail'), 
    path('features/', views.feature_list, name='feature_list'),
    path('feature_id_detail/<int:feature_id>', views.feature_id_detail, name='feature_id_detail'), 
    
    # path('', views.IndexView.as_view(), name='index'),
    # path('bug_detail/<int:bug_id>', views.BugReportDetailView.as_view(), name='bug_detail'), 
    # path('feature_id_detail/<int:feature_id>', views.FeatureRequestDetailView.as_view(), name='feature_id_detail'), 
]