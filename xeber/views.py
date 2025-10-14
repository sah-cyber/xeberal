

# Create your views here.
import requests
from django.shortcuts import render
from .models import IPInfo




def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def ip_view(request):
    ip = get_client_ip(request)

    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = response.json()
    except Exception:
        data = {}

    loc = data.get('loc')
    lat = lon = None
    if loc:
        parts = loc.split(',')
        if len(parts) == 2:
            lat, lon = parts[0], parts[1]

    # DB-ə qeyd et (sadə save, duplicate yoxlamır)
    ipinfo = IPInfo.objects.create(
        ip=ip,
        city=data.get('city', ''),
        region=data.get('region', ''),
        country=data.get('country', ''),
        org=data.get('org', ''),
        lat=lat or '',
        lon=lon or ''
    )

    context = {
        'ip': ip,
        'city': data.get('city', 'Bilinmir'),
        'region': data.get('region', ''),
        'country': data.get('country', ''),
        'org': data.get('org', 'Bilinmir'),
        'lat': lat,
        'lon': lon,
    }

    return render(request, 'ip.html', context)

def index(request):
    context = {


    }
    return render(request, 'index.html',context)


