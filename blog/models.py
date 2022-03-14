from re import template
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from stream import blocks


class BlogListingPage(Page):
    """blog list page contains all blogs created"""
    
    template = 'blog/blog_list.html'
    
    blog_list_title = models.CharField(max_length=100, blank=False, null=False)

    content_panels = Page.content_panels+[

        FieldPanel('blog_list_title'),
    ]

    def get_context(self, request, *args, **kwargs):
        """
            context method for getting the data of DetailPage which will lived in the listing page
            so to access this data there is 2 ways:
            1. by context
            2. by make it as a child
        """
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = BlogDetailPage.objects.live().public() 
        return context


class BlogDetailPage(Page):
    """blog detail page contains all data about a single blog page"""
    
    template = 'blog/blog_detail.html'

    blog_title = models.CharField(max_length=100, blank=False, null=False)
    blog_text = models.TextField(blank=False, null=False)
    blog_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

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
        MultiFieldPanel([
            FieldPanel('blog_title'),
            FieldPanel('blog_text'),
            ImageChooserPanel('blog_image'),
        ], heading='blog detail info'),
        
        MultiFieldPanel([
            StreamFieldPanel('content_body')
        ], heading='stream fields section')
    ]


