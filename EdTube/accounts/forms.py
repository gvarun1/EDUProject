from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Teacher, Student

class TeacherRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    first_name = forms.CharField(max_length=55, required=True)
    last_name = forms.CharField(max_length=55, required=True)
    blood_type = forms.CharField(max_length=5)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'address',
            'first_name',
            'last_name',
            'blood_type',
        ]

    @transaction.atomic
    def save(self):
        print("CHECK CHECK")
        user = super().save(commit=False)
        user.type = CustomUser.UserTypes.TEACHER
        user.email = self.cleaned_data.get('email')
        user.address = self.cleaned_data.get('address')
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.first_name = self.cleaned_data.get('first_name')
        teacher.last_name = self.cleaned_data.get('last_name')
        teacher.blood_type = self.cleaned_data.get('blood_type')
        teacher.save()
        return user

class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    first_name = forms.CharField(max_length=55, required=True)
    last_name = forms.CharField(max_length=55, required=True)
    blood_type = forms.CharField(max_length=5)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'address',
            'first_name',
            'last_name',
            'blood_type',
        ]

    @transaction.atomic
    def save(self):
        print("CHECK CHECK")
        user = super().save(commit=False)
        user.type = CustomUser.UserTypes.STUDENT
        user.email = self.cleaned_data.get('email')
        user.address = self.cleaned_data.get('address')
        user.save()
        student = Student.objects.create(user=user)
        student.first_name = self.cleaned_data.get('first_name')
        student.last_name = self.cleaned_data.get('last_name')
        student.blood_type = self.cleaned_data.get('blood_type')
        student.save()
        return user
