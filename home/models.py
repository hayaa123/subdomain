from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel ,StreamFieldPanel, FieldPanel, MultiFieldPanel
from streams import blocks ,website1bocks
from wagtail.core.fields import StreamField
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel 
from modelcluster.fields import ParentalKey 
from wagtail.snippets.edit_handlers import SnippetChooserPanel

class TeacherOrderable(Orderable):
    """
    allow us to select one or more teacher
    """
    page = ParentalKey("home.HomePage",related_name="teachers")
    teacher = models.ForeignKey(
        "home.Teacher",
        on_delete = models.CASCADE,
    )

    panels = [
        SnippetChooserPanel("teacher")
    ]

class Teacher(models.Model):
    """
    teacher model for snippets
    """
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+"
    )

    panels = [MultiFieldPanel(
        [
            FieldPanel("name"),
            ImageChooserPanel("image")
        ],
        heading="name and Image"
    ),
        MultiFieldPanel([
            FieldPanel("website")
        ],
        heading="link"
        )
    ]

    def __str__(self) -> str:
        return self.name
    class Meta :
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

register_snippet(Teacher)


class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1
    subpage_types = ['flexPage.FlexPage']
    parent_page_types = ['wagtailcore.Page']
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
        StreamFieldPanel("content"),
        InlinePanel("teachers",label="teacher",min_num=1,max_num=4)
       ]


    # def get_context(self, request, *args, **kwargs):
    #     context= super().get_context(request, *args, **kwargs)
    #     # if else statments 
    #     context['p'] = HomePage.objects.all()
    #     return context

# all have the same template ???!! 
class HomePageWebsite1(Page):
    template = "home/home_page_website1.html"
    max_count = 1
    subpage_types = ['flexPage.FlexPageWebsite1']
    parent_page_types = ['wagtailcore.Page']

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
    max_count = 1

