from re import template
from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel ,StreamFieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel 
from modelcluster.fields import ParentalKey 
from wagtail.snippets.edit_handlers import SnippetChooserPanel



from wagtail.core.fields import StreamField
from streams import blocks, website1bocks
# Create your models here.

class FlexPage(Page):
    template ='flexPage/flex_page.html'
    parent_page_types = ['home.HomePage']

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
    parent_page_types = ['home.HomePageWebsite1']

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

