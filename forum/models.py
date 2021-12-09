from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField() # no max length.
    # post_date = models.DateTimeField(auto_now_add=True) <-- can't update date time
    post_date = models.DateTimeField(default=timezone.now) # updates time with timezone import
    author = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE is used to delete posts of deleted users
    # author = models.ForeignKey(User, on_delete=models.SET_DEFAULT) # on user delete, set user to default/[deleted user]


    # for db objects to have their title as their object name
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})