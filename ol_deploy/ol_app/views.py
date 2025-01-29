from django.shortcuts import render

def frontend(request):
    return render(request, "ol_app/map.html")

