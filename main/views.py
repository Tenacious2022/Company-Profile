from urllib import request
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def services(request):
    return render(request, 'services.html')

def industry(request):
    return render(request, 'industry.html')

def clients(request):
    return render(request, 'clients.html')

def products(request):
    return render(request, 'products.html')

def premium_view(request):
    return render(request, 'premium.html')

def cctv_view(request):
    return render(request, 'cctv.html')

def ac_view(request):
    return render(request, 'ac.html')

def wifi_view(request):
    return render(request, 'wifi.html')

def contact_view(request):
    return render(request, 'contact.html')

def product_detail(request, product_slug):
    product_data = {
        'premium': {
            'name': 'Insurance Premium Collection Tools',
            'description': 'Applications and solutions including FS Pro, POS, eRoaster, and digitalization development.'
        },
        'ac': {
            'name': 'Air Conditioners Installations',
            'description': 'Expert installation services for air conditioning systems.'
        },
        'cctv': {
            'name': 'CCTV Solutions',
            'description': 'Reliable CCTV installations and monitoring solutions.'
        },
        'wifi': {
            'name': 'Public WIFI Installations and Maintenance',
            'description': 'Comprehensive public WIFI installation and ongoing maintenance services.'
        }
    }
    
    product = product_data.get(product_slug, {})
    return render(request, 'product_detail.html', {
        'product_name': product.get('name', 'Product Not Found'),
        'product_description': product.get('description', 'No description available.')
    })


