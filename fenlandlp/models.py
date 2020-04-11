'''
Models for the `fenlandlp` Django app
'''


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from accounts.models import Client


class Post(models.Model):
    '''
    Defines database table structure for `Post` entries

    Insert description of what a `Post` is for here
    '''

    DRAFT = 0
    PUBLISHED = 1

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'))

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta: # pylint: disable=missing-class-docstring,too-few-public-methods
        ordering = ['-created_on']

    def get_absolute_url(self):
        '''
        Returns the detail view url for a single `Post` entry
        '''

        return reverse('fenlandlp:post_detail', kwargs={"slug": self.slug})

    def __str__(self):
        '''
        Defines the string returned by the `str()` method when called on a single `Post` entry
        '''

        return self.title


class Comment(models.Model):
    '''
    Defines database table structure for `Comment` entries

    Insert description of what a `Comment` is for here
    '''

    active = models.BooleanField(default=False)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(max_length=100, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: # pylint: disable=missing-class-docstring,too-few-public-methods
        ordering = ['created_on']

    def __str__(self):
        '''
        Defines the string returned by the `str()` method when called on a single `Comment` entry
        '''


        return "Comment {} by {}".format(self.body, self.user)
