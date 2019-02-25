from django.db import models

# Create your models here.

"""
임시로 blog/models.py에서 그대로 복붙한 것임. 나중에 다시 수정 예정.

"""
from django.db import models
from django.utils import timezone


class firstpage(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title