from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topicis inserted successfully')
def insert_webpage(request):
    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    a=input('enter address')
    
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,address=a)[0]
    WO.save()
    return HttpResponse('webpage data is inserted')
def insert_Accessrecords(request):
    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    a=input('enter address')
    n=input('enter name')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,address=a)[0]
    WO.save()

    au=input('enter author')
    amo=input('enter amount')

    AR=Accessrecords.objects.get_or_create(name=WO,author=au,amo=amo)[0]
    AR.save()
    return HttpResponse('Accessrecord data is successfully')

