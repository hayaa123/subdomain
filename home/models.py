from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel ,StreamFieldPanel
from streams import blocks ,website1bocks
from wagtail.core.fields import StreamField

class HomePage(Page):
    template = "home/home_page.html"
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("cta",blocks.CTABlock()),
            ("card",blocks.CardBlock()),
        ],
        null=True,
        blank=True
        )
        


    content_panels = Page.content_panels +[
        StreamFieldPanel("content")
       ]


    # def get_context(self, request, *args, **kwargs):
    #     context= super().get_context(request, *args, **kwargs)
    #     # if else statments 
    #     context['p'] = HomePage.objects.all()
    #     return context

# all have the same template ???!! 
class HomePageWebsite1(Page):
    template = "home/home_page_website1.html"

    content = StreamField(
        [
            ("title_and_text", website1bocks.TitleAndTextBlock()),
            ("cta",website1bocks.CTABlock()),
            ("card",website1bocks.CardBlock()),

        ],
        null=True,
        blank=True
    )
    content_panels = Page.content_panels +[
        StreamFieldPanel("content")
       ]


class HomePageWebsite2(HomePage):
    template = "home/home_page_website2.html"
