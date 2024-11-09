from email.policy import default

from django.db import models

from users.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField("Name slug", max_length=70)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField("Name slug", max_length=70, blank=True, null=True)
    context = models.TextField()
    date = models.DateTimeField()
    is_free = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name='events', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if self.is_free and self.price is not None:
    #         raise ValueError("Price must be null for free events.")
    #     if not self.is_free and self.price is None:
    #         raise ValueError("Price must be set for paid events.")
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.event.title}'


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f'Favorite by {self.user.username} on {self.event.title}'
