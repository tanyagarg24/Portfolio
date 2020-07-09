from django.shortcuts import render,HttpResponse
from homeapp.models import Contact

# Create your views here.
def index(request):
    context={
    "variable":"this is variable"
    }
    return render(request,"index.html",context)
    

def about(request):
    return render(request,"about.html")
def contact(request):
     if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone= request.POST.get('phone')
        query=request.POST.get('query')
        contact=Contact(name=name,email=email,phone=phone,query=query)
        contact.save()
     return render(request,"contact.html")
    
def services(request):
    return render(request,"services.html")
    
     

