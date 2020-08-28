from django.shortcuts import render
from django.db.models import Q


# Create your views here.

def home(request):
    import json
    import requests
    APIkey = "509b6441-4ced-48fa-b6b7-8128fd74fc88"
    # http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/3840?res=3hourly?key=509b6441-4ced-48fa-b6b7-8128fd74fc88

    # api_request = requests.get("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=509b6441-4ced-48fa-b6b7-8128fd74fc88")
    api_request = requests.get("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/3407?res=daily&key=509b6441-4ced-48fa-b6b7-8128fd74fc88")


    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', { "api" : api })


def about(request):
    return render(request, 'about.html', {})








