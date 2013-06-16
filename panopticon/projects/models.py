from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255)
    github = models.CharField(max_length=255, blank=True)
    done = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    flickr = models.CharField(max_length=100, blank=True)
    wiki = models.CharField(max_length=255, blank=True)
    pad = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    active = models.BooleanField(default=True)


class Participant(models.Model):
    user = models.OneToOneField(User, unique=True)
    owner = models.BooleanField(default=False)
