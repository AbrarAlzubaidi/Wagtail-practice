from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

@register_setting
class SocialMedia(BaseSetting):
    """social media links"""
    facebook = models.URLField(null=True, blank=True, help_text='facebook url')
    github = models.URLField(null=True, blank=True, help_text='github url')

    panels = [
        MultiFieldPanel([ 
            FieldPanel('facebook'),
            FieldPanel('github'),
        ], heading="social media url's")
    ]