from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import IPInfo

@admin.register(IPInfo)
class IPInfoAdmin(admin.ModelAdmin):
    list_display = ('ip', 'city', 'region', 'country', 'org', 'lat', 'lon', 'get_post_img','created_at')
    readonly_fields = ('created_at',)



    def get_post_img(self, obj):
        if obj.image:  # Fayl varsa
            return mark_safe(f"<img src='{obj.image.url}' width='50' />")
        return "Yoxdur"

    get_post_img.short_description = 'image'