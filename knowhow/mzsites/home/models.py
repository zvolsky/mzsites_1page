from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from wagtailmenus.models import MenuPage


class MzPage(MenuPage):
    is_creatable = False
