from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def msd(request):
    return render(request,'msd.html')


def jaddu(request):
    return HttpResponse('<h1>JADDU IS A BEST BOWLER & FIELDER</h1>')