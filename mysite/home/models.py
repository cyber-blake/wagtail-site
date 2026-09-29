from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

class HomePage(Page):
    subtitle = models.CharField(max_length=100, null=True, blank=True, verbose_name='Подзаголовок')
    rtfbody = RichTextField(null=True, blank=True)

    # панели админки 
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtfbody')
    ]