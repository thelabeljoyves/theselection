from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

class TheselectionExtension(PageExtension):
    subtitle = models.CharField(max_length=30)
    backgroundcolor = models.CharField(max_length=9)


extension_pool.register(TheselectionExtension)
