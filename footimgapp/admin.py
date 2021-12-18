from django.contrib import admin
from .models import Footimg


class FootimgAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')


admin.site.register(Footimg, FootimgAdmin)
