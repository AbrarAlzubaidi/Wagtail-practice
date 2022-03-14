from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from stream import blocks

class FlexPage(Page):
    """ flexable page class"""
    template = 'flex/flex_page.html'

    subtitle = models.CharField(max_length=255, null=True, blank=True)
    content_body = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBlock()),
            ("simple_richtext", blocks.SimpleRichTextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels+[
        FieldPanel('subtitle'),
        StreamFieldPanel('content_body')
    ]

    class Meta:
        verbose_name = 'flex page'
        verbose_name_plural = 'flex pages'
