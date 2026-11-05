from django.shortcuts import render
from .models import Portfolio

def index(request):
    #Retrieve active portfolios
    active_portfolios = Portfolio.objects.filter(is_active=True)
    return render(request, 'portfolio_app/index.html', {'active_portfolios':active_portfolios})

from django.views.generic import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = "students"\
        
from django.views.generic import DetailView

class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'