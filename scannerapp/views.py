from django.shortcuts import render
from django.http import HttpResponse
import scapy.all as scapy
import socket

# Create your views here.
def first(request):
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return HttpResponse('IP Address = ' + IPAddr)