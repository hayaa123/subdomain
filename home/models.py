from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    templates = "templates/home/home_page.html"
    home_title = models.CharField(max_length=100,null=True)

    content_panels = Page.content_panels +[
        FieldPanel("home_title"),
       ]

    def get_context(self, request, *args, **kwargs):
        context= super().get_context(request, *args, **kwargs)
        # if else statments 
        context['p'] = HomePage.objects.all()
        return context

# all have the same template ???!! 
# 