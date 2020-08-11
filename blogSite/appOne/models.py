from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, related_name = 'posts')
    title = models.CharField(max_length = 100)
    content = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    publish_date = models.DateTimeField(blank = True, null = True)
    is_published = models.BooleanField(default = False)

    def publish(self):
        self.is_published = True
        print(timezone.now())
        self.publish_date = timezone.now()
        self.save()

    def name(self):
        return '{} {}'.format(user.first_name,user.last_name)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('appOne:myblog', kwargs={'pk': self.pk})

class Comment(models.Model):
    author = models.CharField(max_length=50)
    com_content = models.TextField()
    create_date = models.DateField(default = timezone.now, blank = True)
    post = models.ForeignKey(Post, related_name = 'comments')

    def __str__(self):
        return self.author
