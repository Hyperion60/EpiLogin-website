from django.contrib import admin

from website.apps.servers.models import Server

class ServerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )

admin.site.register(Server, ServerAdmin)
