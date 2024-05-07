from django.http import HttpResponse
from django.shortcuts import render,redirect
from.forms import ContactFormForm,BuyForm
from .models import Buy

# Create your views here.
def home(request):
    return render(request,'main/home.html')
# def contactus(request):
#     return render(request,'main/contactus.html')
def aboutus(request):
    return render(request,'main/aboutus.html')
def blog(request):
    return render(request,'main/blog.html')
def smartphones(request):
    return render(request,'main/smartphones.html')
def laptops(request):
    return render(request,'main/laptops.html')
def wearables(request):
    return render(request,'main/wearables.html')
def blog1(request):
    return render(request,'main/blog1.html')
def blog2(request):
    return render(request,'main/blog2.html')
def contactus(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/contactus.html', {'form': form, 'message': 'Thank you for your message!'})
    else:
        form = ContactFormForm()
    return render(request, 'main/contactus.html', {'form': form})
def Buyfunction(request, product_name, price):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            product_name =product_name
            price = price
            email= form.cleaned_data['email']
            purchase =Buy(product_name=product_name, price=price,email=email,)
            purchase.save()
            # Redirect or render a success page
            return render(request, 'main/Buy.html', {'form':form, 'message': 'Thank you for your message!'})
    else:
        form = BuyForm()
    
    return render(request, 'main/Buy.html',{'form':form,'product_name': product_name, 'price': price})