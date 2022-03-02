import email
from unicodedata import name
from django.forms import Textarea
from django.shortcuts import render
from datetime import date, datetime
from home.models import Contact

def index(request):
    return render(request, 'index.html')

def books(request):
    return render(request, 'books.html')

def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        textarea = request.POST.get('textarea')
        contact = Contact(fname=fname, lname=lname, email=email, textarea=textarea, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')