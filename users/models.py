from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from django.db import models as m

# Create your models here.
roles = [
    ('admin', 'admin'),
    ('user', 'user')
]


class User(AbstractUser):  # is_superuser = admin
    date_of_birth = m.DateField('Date of birth', null=True, blank=True)
    bio = m.TextField(blank=True, null=True)
    role = m.CharField("Role", choices=roles, max_length=50)
    avatar = m.ImageField("avatar", upload_to='profile_pics/', default='default_images/user_icon.png/', blank=True,
                          null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    REQUIRED_FIELDS = ['email']

    def get_age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year - (
                        (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            return age
        return None

    def __str__(self):
        return self.username


# class EmailCodes(m.Model):
#     code = m.IntegerField("Code", validators=[MaxValueValidator(6), MinValueValidator(1)])
