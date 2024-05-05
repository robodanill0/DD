from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('bugs/', views.bug_list, name='bug_list'), 
	path('bug_detail/<int:bug_id>', views.bug_detail, name='bug_detail'), 
    path('features/', views.feature_list, name='feature_list'),
    path('feature_id_detail/<int:feature_id>', views.feature_id_detail, name='feature_id_detail'), 
]