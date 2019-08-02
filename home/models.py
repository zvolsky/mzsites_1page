from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from wagtailmenus.models import MenuPage


class MzPage(MenuPage):
    is_creatable = False


class BasicPage(MzPage):
    template = "home/basic_page.html"

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = MzPage.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _("Basic Page")
        verbose_name_plural = _("Basic Pages")
