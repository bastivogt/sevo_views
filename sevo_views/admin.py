from django.contrib import admin

from . import models

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    fields = [
        "firstname",
        "lastname",
        "birthday"
    ]

    list_display = [
        "firstname",
        "lastname",
        "birthday"
    ]


admin.site.register(models.Person, PersonAdmin)
