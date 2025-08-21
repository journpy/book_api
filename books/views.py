#from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("""
                        Welcome to my Book Management API Project. 
                        Refer to the documentation for publicly available API 
                        endpoints.
                        """)
