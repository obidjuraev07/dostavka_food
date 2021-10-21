from django.shortcuts import render
import requests
api_url = "http://127.0.0.1:8000/api/v1"
def dashboard(request):
    ctx = {}
    return render(request, 'dashboard/index.html',ctx)
def foods_list(request):
    items = requests.get(f"{api_url}/foods/")
    items = items.json()["items"]
    ctx = {
        'items': items
    }
    return render(request, 'dashboard/foods.html', ctx)