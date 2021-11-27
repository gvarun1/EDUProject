from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .models import CustomUser, Teacher, Student
from .forms import TeacherRegistrationForm, StudentRegistrationForm
from classroom.models import Subject

class TeacherRegistrationView(CreateView):
    model = CustomUser
    form_class = TeacherRegistrationForm
    success_url = reverse_lazy('home')
    template_name = '../templates/registration/teacher_registration.html'

class HomePageTest(TemplateView):
    template_name = '../templates/home.html'

class StudentRegistrationView(CreateView):
    model = CustomUser
    form_class = StudentRegistrationForm
    success_url = reverse_lazy('student-dashboard')
    template_name = '../templates/registration/student_registration.html'

class StudentDashboardView(CreateView):
    model = Student
    fields = '__all__'
    template_name = '../templates/dashboards/student_dashboard.html'

class PracticeTestView(ListView):
    model = Subject
    fields = '__all__'
    def get_queryset(self):
        student_classroom = self.request.user.student.classroom
        queryset = super().get_queryset()
        return queryset.filter(classroom =student_classroom)
    template_name = '../templates/student/practice_test_subject.html'
