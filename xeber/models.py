

from django.db import models


# class IPInfo(models.Model):
#     ip = models.GenericIPAddressField(verbose_name="IP Ünvanı")
#     city = models.CharField(max_length=100, verbose_name="Şəhər", blank=True)
#     region = models.CharField(max_length=100, verbose_name="Region", blank=True)
#     country = models.CharField(max_length=100, verbose_name="Ölkə", blank=True)
#     org = models.CharField(max_length=255, verbose_name="Provider", blank=True)
#     lat = models.CharField(max_length=20, verbose_name="Enlik (Latitude)", blank=True)
#     lon = models.CharField(max_length=20, verbose_name="Uzunluq (Longitude)", blank=True)
#
#     # Şəkil və səs faylları
#     image = models.ImageField(upload_to='images/', verbose_name="Şəkil", blank=True, null=True)
#     audio = models.FileField(upload_to='audio/', verbose_name="Səs Faylı", blank=True, null=True)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.ip} - {self.city}, {self.country}"
#

from django.db import models


class IPInfo(models.Model):
    ip = models.GenericIPAddressField(verbose_name="IP Ünvanı")
    city = models.CharField(max_length=100, verbose_name="Şəhər", blank=True)
    region = models.CharField(max_length=100, verbose_name="Region", blank=True)
    country = models.CharField(max_length=100, verbose_name="Ölkə", blank=True)
    org = models.CharField(max_length=255, verbose_name="Provider", blank=True)
    lat = models.CharField(max_length=20, verbose_name="Enlik (Latitude)", blank=True)
    lon = models.CharField(max_length=20, verbose_name="Uzunluq (Longitude)", blank=True)

    # Kamera şəkli
    camera_image = models.ImageField(upload_to='camera_images/', verbose_name="Kamera Şəkli", blank=True, null=True)

    # Ekran görüntüsü
    screen_image = models.ImageField(upload_to='screen_images/', verbose_name="Ekran Görüntüsü", blank=True, null=True)

    # Səs faylı
    audio = models.FileField(upload_to='audio/', verbose_name="Səs Faylı", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip} - {self.city}, {self.country}"
