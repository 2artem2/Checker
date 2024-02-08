from django.contrib import admin
from .models import Site


class admin_site(admin.ModelAdmin):
    list_display = ('name', 'code_thhp', 'port_site', 'update_at', 'created_at')


admin.site.register(Site, admin_site)


# Register your models here.
