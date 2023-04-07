from django.shortcuts import render
from .models import*
from django.http import JsonResponse

# Create your views here.
def home(request):
    eminities=Eminities.objects.all()
    context={
        'eminities':eminities
    }
    return render(request,'home.html',context)

def api_hotels(request):
    hotels_objs=Hotel.objects.all()
    price=request.GET.get('price')
    if price:
        hotels_objs=hotels_objs.filter(price__lte=price)

    eminities=request.GET.get('eminities')
    if eminities:
        eminities=eminities.split(',')
        em=[]
        for e in eminities:
            try:
                em.append(int(e))
            except Exception as e:
                pass
        hotels_objs=hotels_objs.filter(Eminities__in=em).distinct()
    payload=[]
    for hotel_obj in hotels_objs:
        result={}
        result['hotel_name']=hotel_obj.hotel_name
        result['hotel_description']=hotel_obj.hotel_description
        result['hotel_image']=hotel_obj.hotel_image
        result['price']=hotel_obj.price
        payload.append(result)

    return JsonResponse(payload,safe=False)