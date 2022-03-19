from email.policy import default
from django.db import models

# Create your models here.
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Page
# from wagtail.admin.edit_handlers import FieldPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

@register_setting
class ColorSetting(BaseSetting):
    color1 = ColorField(default='#0E3EDA')
    color2 = ColorField(default='#F473B9')
    color3 = ColorField(default='#FFBDE6')

    content_panels = Page.content_panels +[
                NativeColorPanel('color1'),
                NativeColorPanel('color2'),
                NativeColorPanel('color3'),
       ]