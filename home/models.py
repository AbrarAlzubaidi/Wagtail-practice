from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel , InlinePanel, PageChooserPanel,StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from stream import blocks

class HomePageCarouselImages(Orderable):
    """home page carousel"""
    page = ParentalKey('home.HomePage', related_name='carousel_images')
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        ImageChooserPanel('image')
    ]

class HomePage(RoutablePageMixin, Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_body = StreamField(
        [
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [        
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
        ], heading='home page settings'),

        MultiFieldPanel([ 
            InlinePanel('carousel_images', max_num=3, min_num=1, label='add image for carousel'),
        ], heading='home page carousel images'),

        MultiFieldPanel([ 
            StreamFieldPanel('content_body'),
        ], heading='stream fiels section')

    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

    @route(r'^subscribe/$')
    def the_subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)

        # return context --> if we used get_context method but here we use something different
        return render(request, "subscriber/subscriber.html" , context)