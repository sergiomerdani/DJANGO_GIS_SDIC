from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def frontend(request):
    return render(request, "ol_app/map.html")

