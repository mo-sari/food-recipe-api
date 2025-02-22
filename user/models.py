from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('email field can not be empty')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'


class Profile(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/',
                              null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'profile for {self.user.name}'

    class Meta:
        db_table = 'profile'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
