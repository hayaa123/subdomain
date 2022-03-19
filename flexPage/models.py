from re import template
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel ,StreamFieldPanel
from wagtail.core.fields import StreamField
from streams import blocks, website1bocks
# Create your models here.

class FlexPage(Page):
    template ='flexPage/flex_page.html'
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("cta",blocks.CTABlock()),
            ("card",blocks.CardBlock()),
            ("richtext",blocks.RichTextBlock()),
        ],
        null=True,
        blank=True
        )
    
    content_panels = Page.content_panels +[
        StreamFieldPanel("content")
       ]

class FlexPageWebsite1(Page):
    template ='flexPage/flex_page.html'
    content = StreamField(
        [
            ("title_and_text", website1bocks.TitleAndTextBlock()),
            ("cta",website1bocks.CTABlock()),
            ("card",website1bocks.CardBlock()),
            ("richtext",website1bocks.RichTextBlock()),
        ],
        null=True,
        blank=True
        )
    
    content_panels = Page.content_panels +[
        StreamFieldPanel("content")
       ]
