from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    """ Manager for the CustomUser model"""
    def create_user(self, email, password=None, **extra_fields):
        """Creating an user (basic super)"""
        if not email:
            raise ValueError("Users must have email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user