from django.urls import path
from .views import TeacherListView,CourseListView,CourseDetailView,CourseUpdateView,CourseDeleteView,AddCourseView
urlpatterns = [
    path('teachers/',TeacherListView.as_view(),name='teachers'),
    path('course/',CourseListView.as_view(),name='courses'),
    path('course/<int:id>/',CourseDetailView.as_view(),name='course-detail'),
    path('update/<int:id>',CourseUpdateView.as_view(),name='course-update'),
    path('delete/<int:id>/',CourseDeleteView.as_view(),name='course-delete'),
    path('add_course/',AddCourseView.as_view(),name='course-add'),
]