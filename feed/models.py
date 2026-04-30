from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title #when django prints an object it will show the title instead of post.object

    class Meta:
        ordering = ['-posted_on']   #comes in recent posts

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'id':self.id}) #returns url of an obj of post
