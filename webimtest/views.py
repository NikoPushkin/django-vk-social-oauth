from django.shortcuts import render, redirect

def app_redirect(request):
    return redirect('fivefriends/')
