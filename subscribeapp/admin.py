from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')


admin.site.register(Subscription, SubscriptionAdmin)
