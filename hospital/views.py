from django.shortcuts import render, redirect
from . models import Department
from . models import Doctor
from . forms import BookingForm

def index(request):
    item = Department.objects.all()
    doc = Doctor.objects.all()
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
            return redirect("/")
    form=BookingForm()
    context={
        "item":item,
        "doc":doc,
        "form":form
    }
    return render(request,"index.html",context)
def error(request):
    return render(request,"404.html")
def blog(request):
    return render(request,"blog-single.html")
def contact(request):
    return render(request,"contact.html")
def port(request):
    return render(request,"protfolio-detail.html")