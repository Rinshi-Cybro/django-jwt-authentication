from django.urls import path
from .views import DepartmentListView, StudentListView, BranchListView


urlpatterns = [
    # URL pattern for getting details of a specific student by ID
    path('student/<int:pk>/', StudentListView.as_view(), name='student-detail'),
    path('students/', StudentListView.as_view(), name='student-list')
]
