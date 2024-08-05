from django.urls import path
from student.views import StudentView

urlpatterns = [
    path('get/', StudentView.as_view({'get': 'get_students'})),
    path('get/<int:pk>/', StudentView.as_view({'get': 'get_student'})),
    path('create/', StudentView.as_view({'post': 'create_student'})),
    path('update/', StudentView.as_view({'put': 'update_student'})),
    path('delete/<int:pk>/', StudentView.as_view({'delete': 'delete_student'})),
]
