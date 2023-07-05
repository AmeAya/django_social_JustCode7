from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # reverse - это перессылка на другой ulr/view


# Create your models here.
class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return str(self.title) + ' - ' + str(self.author.username)

    def get_absolute_url(self):
        return reverse('posts_list')
