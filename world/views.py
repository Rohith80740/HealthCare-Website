from tkinter import Grid
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def price(request):
    return render(request,'price.html')
def blog(request):
    return render(request,'blog.html')
def detail(request):
    return render(request,'detail.html')
def team(request):
    return render(request,'team.html')
def testimonial(request):
    return render(request,'testimonial.html')
def appointment(request):
    return render(request,'appointment.html')
def search(request):
    return render(request,'search.html')
def contact(request):
    return render(request,'contact.html')                            
        
  
     
 


