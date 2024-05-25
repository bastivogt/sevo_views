from django.contrib import admin

from . import models

# Register your models here.


class MemmberAdmin(admin.ModelAdmin):
    list_display = [
        "firstname",
        "lastname",
        "birthday"
    ]

admin.site.register(models.Member, MemmberAdmin)
