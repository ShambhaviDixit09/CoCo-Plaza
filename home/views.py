from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contacts
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    # form = CitySearchForm(request.GET)
    # if form.is_valid():
    #     city_name = form.cleaned_data['city']
    #     # Perform the search query using the city name
    #     cities = City.objects.filter(name__icontains=city_name)
    # else:
    #     cities = City.objects.none()

    # context = {
    #     'form': form,
    #     'cities': cities
    # }
    return render(request, 'about.html')
    # return render(request, 'about.html')

def services(request):
      return render(request, 'services.html')

def contacts(request):
    if request.method == 'POST':
         name = request.POST.get('name')
         phone = request.POST.get('phone')
         email = request.POST.get('email')
         desc = request.POST.get('desc')
         contact = Contacts(name= name, email= email, phone= phone, desc= desc, date = datetime.today())

         contact.save()
         messages.success(request, "Your message has been sent!!")
    return render(request, 'contacts.html')

def cocoClub(request):
    return render(request, 'cocoClub.html')
         

    return render(request, 'contacts.html')
    # return HttpResponse('This is contacts page')

