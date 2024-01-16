from django.shortcuts import render
from django.http.response import HttpResponse

# Created views here

def registerUser(request):
    return HttpResponse('This is a user registration form')
