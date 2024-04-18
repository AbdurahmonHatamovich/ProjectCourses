from django.urls import path
from .views import TeacherListView,CourseListView
urlpatterns = [
    path('teachers/',TeacherListView.as_view(),name='teachers'),
    path('course/',CourseListView.as_view(),name='courses'),
]