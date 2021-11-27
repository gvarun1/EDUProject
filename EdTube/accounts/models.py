from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin

#Non Django imports
from .managers import CustomUserManager
#from classroom.models import Classroom
# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    address = models.TextField(max_length=500)
    #phone_number = models.PositiveBigIntegerField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    #is_student = models.BooleanField(default=True)
    #is_teacher = models.BooleanField(default=False)


    class UserTypes(models.TextChoices):
        TEACHER = "Teacher", "TEACHER"
        STUDENT = "Student", "STUDENT"

    default_type = UserTypes.STUDENT
    type = models.CharField(_('UserType'), max_length=255, choices=UserTypes.choices, default=default_type)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



class School(models.Model):
    #ADD unique fields
    school_name = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name

class Teacher(models.Model):
    #ADD unique fields
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #school = models.ForeignKey(School, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    blood_type = models.CharField(max_length=5)
    #emergency_contact = models.PositiveBigIntegerField()

    def __str__(self):
        return self.first_name + self.last_name

class Student(models.Model):
    #ADD unique fields
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #school = models.ForeignKey(School, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    blood_type = models.CharField(max_length=5)
    emergency_contact = models.PositiveBigIntegerField()
    father_name = models.CharField(max_length=55)
    mother_name = models.CharField(max_length=55)
    father_contact_number = models.PositiveBigIntegerField()
    mother_contact_number = models.PositiveBigIntegerField()
    father_occupation = models.CharField(max_length=55)
    mother_occupation = models.CharField(max_length=55)

    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name
