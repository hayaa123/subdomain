from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel ,StreamFieldPanel
from streams import blocks ,website1bocks
from wagtail.core.fields import StreamField

class HomePage(Page):
    templates = "templates/home/home_page.html"
    home_title = models.CharField(max_length=100,null=True)
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("cta",blocks.CTABlock())
        ],
        null=True,
        blank=True
        )
        


    content_panels = Page.content_panels +[
        FieldPanel("home_title"),
        StreamFieldPanel("content")
       ]


    # def get_context(self, request, *args, **kwargs):
    #     context= super().get_context(request, *args, **kwargs)
    #     # if else statments 
    #     context['p'] = HomePage.objects.all()
    #     return context

# all have the same template ???!! 
# 
class HomePageWebsite1(Page):
    templates = "templates/home/home_page_website1.html"
    home_title = models.CharField(max_length=100,null=True)

    content = StreamField(
        [
            ("title_and_text", website1bocks.TitleAndTextBlock()),
            ("cta",website1bocks.CTABlock())
        ],
        null=True,
        blank=True
    )
    content_panels = Page.content_panels +[
        FieldPanel("home_title"),
        StreamFieldPanel("content")
       ]


class HomePageWebsite2(HomePage):
    templates = "templates/home/home_page_website2.html"
