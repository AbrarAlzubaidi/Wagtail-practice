from tabnanny import verbose
from django.db import models

class Subscribers(models.Model):
    """subscribers django model"""
    template = 'subscriber/subscriber.html'

    email = models.CharField(max_length=500, blank=False, null=False, help_text='email address')
    name = models.CharField(max_length=100, blank=False, null=False, help_text='full name')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    # any django model if i want to add it into wagtail pages we can
    # 1. register it as a snippet
    # 2. using orderable (if case needed)
    # 3. modeladmin_register (which is used with subscribers app)