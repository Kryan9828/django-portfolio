from django.shortcuts import render
from .models import Portfolio
from .models import Project

def index(request):
    #Retrieve active portfolios
    active_portfolios = Portfolio.objects.filter(is_active=True)
    return render(request, 'portfolio_app/index.html', {'active_portfolios':active_portfolios} )

from django.views.generic import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'
        
from django.views.generic import DetailView

class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_list.html'
    context_object_name = 'portfolios'
    
class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_detail.html'
    context_object_name = 'portfolio'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super(DetailView,self).get_context_data(**kwargs)
        context["projects"] = Project.objects.all() 
        return context
    
    