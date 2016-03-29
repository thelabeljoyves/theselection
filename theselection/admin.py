from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import TheselectionExtension


class TheselectionExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(TheselectionExtension, TheselectionExtensionAdmin)