from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    FieldPanel ,
    StreamFieldPanel,
    ObjectList,
    MultiFieldPanel,
    TabbedInterface)
from streams import blocks
from wagtail.core.fields import StreamField

class HomePage(Page):
    template = "home/home_page.html"
    home_title = models.CharField(verbose_name="home_title",max_length=100,null=True)
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("cta",blocks.CTABlock()),
            ("card",blocks.CardBlock()),
        ],
        null=True,
        blank=True
        )
    def get_context(self, request, *args, **kwargs):
            context =  super().get_context(request, *args, **kwargs)
            context['url']=f"{self.url_path[1:-1]}_base.html"
            return context


    content_panels = Page.content_panels +[
        StreamFieldPanel("content")
       ]
    # promote_panels = []
    # settings_panels = []
    sidebar_panels = [
        MultiFieldPanel(
            [
                FieldPanel('home_title')
            ],heading='text'
        )
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels,heading= "content"),
            ObjectList(Page.promote_panels,heading='Promotion'),
            ObjectList(Page.settings_panels,heading='settings'),
            ObjectList(sidebar_panels,heading='Side Panels'), 
        ]
    )


HomePage._meta.get_field("title").verbose_name = 'new verbose name' 
HomePage._meta.get_field("title").help_text = 'abrar want to change this'
HomePage._meta.get_field('title').default = "HOME"
# HomePage._meta.get_field('slug').d efault = HomePage.home_title.

