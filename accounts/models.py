from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, full_name, contact_number, password=None):
        if not email:
            raise ValueError('email required!!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, full_name=full_name, contact_number=contact_number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, full_name, contact_number, password=None):
        user = self.create_user(email=email, username=username, full_name=full_name, contact_number=contact_number, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', 'contact_number']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

    def clean(self):
        if not self.contact_number.isdigit() or len(self.contact_number) != 10:
            raise ValidationError('Please enter 10 digit contact number')



@receiver(post_save, sender=CustomUser)
def assign_default_group(sender, instance, created, **kwargs):
    if created:
        default_group = Group.objects.get(name='default_group')
        if instance.is_superuser == False:
            instance.groups.add(default_group)
            instance.save()
            print('worked---')
    print('signal recieved---')