"""
Streamfield live in here
"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """
    title and text
    """

    title = blocks.CharBlock(required=True, help_text="title", max_length=100)
    text = blocks.TextBlock(
        required=True, help_text="the text content goes here")

    class Meta:
        template = "streams/title_and_text_Block.html"
        icon = "edit"
        label = "Title and text"

class CTABlock(blocks.StructBlock):
    """
    A simple call to action section
    """
    title = blocks.CharBlock(required=True , max_length=50)
    text = blocks.RichTextBlock(required=True , features=["bold","italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True,default="Learn More",max_length=20)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to action "



class RichTextBlock(blocks.RichTextBlock):
    """rich text block"""

    class Meta:
        template = 'streams/richtext_block.html'
        lable = 'Full-RichText'
        icon = "doc-full"



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
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"


# class LinkStructValue(blocks.StructValue):
#     """
#     additional logic for our urls
#     """
#     def url(self):
#         button_page = self.get('button_page')
#         button_url = self.get('button_url')
#         if button_page:
#             return button_page.url
#         elif button_url:
#             return button_url

#         return None