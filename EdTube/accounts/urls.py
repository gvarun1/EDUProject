from django.contrib import admin
from django.urls import path, include

from .views import TeacherRegistrationView, HomePageTest, StudentRegistrationView, StudentDashboardView,PracticeTestView

urlpatterns = [
   path("", HomePageTest.as_view(), name='home'),
   path("teacher-registration/", TeacherRegistrationView.as_view(), name='teacher-registration'),
#    path("teacher-login/", TeacherLoginView.as_view(), name='teacher-login'),
   path("student-registration/", StudentRegistrationView.as_view(), name='student-registration'),
   path("student-dashboard/",StudentDashboardView.as_view(), name='student-dashboard'),
   path("practice-test/select-subject/",PracticeTestView.as_view(), name='practice-test'),
]
