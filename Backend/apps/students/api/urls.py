from django.urls import path
from .views import DepartmentListView, StudentListView, BranchListView


urlpatterns = [
    #URL pattern for getting details of a specific department by ID
    path('branch/<int:pk>/', BranchListView.as_view(), name='branch-detail'),
    path('branches/', BranchListView.as_view(), name='branch-list'),

    # URL pattern for getting details of a specific department by ID
    path('department/<int:pk>/', DepartmentListView.as_view(), name='department-detail'),
    path('departments/', DepartmentListView.as_view(), name='department-list'),

    # URL pattern for getting details of a specific student by ID
    path('student/<int:pk>/', StudentListView.as_view(), name='student-detail'),
    path('students/', StudentListView.as_view(), name='student-list')
    
]
