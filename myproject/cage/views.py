from django.shortcuts import render
from .models import Monster
from django.http import HttpResponse

def index(request):
    context = {"monsters": Monster.objects.all()}
    return render (request, "cage/index.html", context)

def detail(request, scp_id):
    context = {"monster": Monster.objects.get(pk=scp_id)}
    return render (request, "cage/profile.html", context)

    # return HttpResponse(m.monster_name)
