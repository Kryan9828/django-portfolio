from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name = 'student-detail'),
    path('portfolios/', views.PortfolioListView.as_view(), name = 'portfolio-list'),
    path('portfolios/<int:pk>', views.PortfolioDetailView.as_view(), name = 'portfolio-detail')
]
