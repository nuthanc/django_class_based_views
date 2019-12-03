from django.urls import path, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    re_path(r'^(?P<pk>\d+)/$', views.SchoolDetailedView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create')
]
