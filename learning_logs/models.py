from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, default='')  # slugfield limited to 50 chars by default
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

    def get_absolute_url(self):
        return reverse('topic_by_slug', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(Topic, self).save(*args, **kwargs)

class Entry(models.Model):
    """Something specific learned about a topic"""
    # each entry must have a topic (single) - may want multiple topics?
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    slug = models.SlugField(max_length=100, default='')
    date_added = models.DateTimeField(auto_now_add=True)

    # def get_absolute_url(self):
    #     return reverse('entry_by_slug', kwargs={'slug': self.slug})


    class Meta:
        # force database to be named plural correctly, rather than entrys
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
