from django.urls import path
from lmsapp.views import (RegisterView ,StudentListCreateView,StudentRetrieveUpdateDestroyAPIView, TeacherListCreateView,TeacherRetrieveUpdateDestroyAPIView,ProtectedView,EnrollmentListCreateView,EnrollmentRetrieveUpdateDestroyAPIView,LessonListCreateView,LessonRetrieveUpdateDestroyAPIView,
AssignmentListCreateView,AssignmentRetrieveUpdateDestroyAPIView,SubmissionListCreateView,SubmissionRetrieveUpdateDestroyAPIView,LessonListCreateView,LessonRetrieveUpdateDestroyAPIView,CourseListCreateView,CourseRetrieveUpdateDestroyAPIView)
from .views import LoginView
urlpatterns = [
    
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/protected/", ProtectedView.as_view(), name="protected"),
    path("api/teacher/", TeacherListCreateView.as_view(), name="teacher-list"),
    path('api/teacher/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name="teacher-detail"),
    path("api/student/"  , StudentListCreateView.as_view(), name="student-list"),
    path("api/student/<int:pk>/", StudentRetrieveUpdateDestroyAPIView.as_view(), name="student-detail"),
    path("api/course/", CourseListCreateView.as_view(), name="course-list"),
    path("api/course/<int:pk>/", CourseRetrieveUpdateDestroyAPIView.as_view(), name="course-detail"),
    path("api/lesson/", LessonListCreateView.as_view(), name="lesson-list"),
    path("api/lesson/<int:pk>/", LessonRetrieveUpdateDestroyAPIView.as_view(), name="lesson-detail"),
    path("api/enrollment/", EnrollmentListCreateView.as_view(), name="enrollment-list"),
    path("api/enrollment/<int:pk>/", EnrollmentRetrieveUpdateDestroyAPIView.as_view(), name="enrollment-detail"),
    path("api/lesson/", LessonListCreateView.as_view(), name="lesson-list"),
    path("api/lesson/<int:pk>/", LessonRetrieveUpdateDestroyAPIView.as_view(), name="lesson-detail"),
    path("api/assignment/", AssignmentListCreateView.as_view(), name="assignment-list"),
    path("api/assignment/<int:pk>/", AssignmentRetrieveUpdateDestroyAPIView.as_view(), name="assignment-detail"),
    path("api/submission/", SubmissionListCreateView.as_view(), name="submission-list"),
    path("api/submission/<int:pk>/", SubmissionRetrieveUpdateDestroyAPIView.as_view(), name="submission-detail"),
    
]
