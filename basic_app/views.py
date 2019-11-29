from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models
# Create your views here.
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailedView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
