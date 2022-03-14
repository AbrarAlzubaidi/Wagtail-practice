"""blocks of all stream field """

from urllib import request
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    """title and text block"""
    title = blocks.CharBlock(
        required=True,
        help_text='add your title here :)'
    )
    text = blocks.TextBlock(required=True, help_text='add your text/paragraph here :)')

    class Meta:
        template = 'stream/title_text_block.html'
        lable = 'title And text'
        icon = 'edit'


class RichTextBlock(blocks.RichTextBlock):
    """rich text block"""

    class Meta:
        template = 'stream/richtext_block.html'
        lable = 'Full-RichText'
        icon = "doc-full"

class SimpleRichTextBlock(blocks.RichTextBlock):
    """rich text block with limited text styles"""
    def __init__(self, required=True, help_text=None, editor="default", features=None, **kwargs):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link", 'h1', 'h2']

    class Meta: 
        template = "stream/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class CardBlock(blocks.StructBlock):
    """card block using listblock"""
    title = blocks.CharBlock(
        required=True,
        help_text='add your title here :)'
    )
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False, help_text="If the button page above is selected, it will be used first.")),
                ("button_url", blocks.URLBlock(required=False, )),
            ]
        )
    )

    class Meta: 
        template = "stream/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"


class CTABlock(blocks.StructBlock):
    """call to action block (CTA)"""
    title = blocks.CharBlock(required=True, max_length=100, help_text='add your title here :)')
    text = blocks.TextBlock(required=True, help_text='add your text/paragraph here :)')
    # inner url (choose a link from wagtail pages)
    button_page = blocks.PageChooserBlock(required=False)
    # external url (ex: https://www.google.com/)
    button_url = blocks.URLBlock(required=False)
    # the text that will be inside the button strucure (ex: learn more)
    button_text = blocks.CharBlock(required=True, max_length=50)
    

    class Meta: 
        template = "stream/cta_block.html"
        icon = "placeholder"
        label = "Call To Action"
