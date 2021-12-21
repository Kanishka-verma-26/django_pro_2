from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import *

# Create your views here.
def fir_func(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dict = {'insert_me':'Hello everyone my name is kanishka verma'}
    return render(request,'registration.html',context=date_dict)

def sec_func(request):
    return HttpResponse('In italics : <em>MY SECOND APP</em><br><span> In bold : <h1 style= "display:inline": top>MY SECOND APP</h1></span>')