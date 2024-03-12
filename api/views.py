from django.shortcuts import render ,HttpResponse
from api.models import student
from api.serili import st
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt


def viee(req):
    d=student.objects.get(id=1)
    ser=st(d)
    jdata=JSONRenderer().render(ser.data)
    return HttpResponse(jdata)
   
@csrf_exempt
def vie(req):
    if req.method == 'POST':
        a = req.body
        strim=io.BytesIO(a)
        pathondata=JSONParser().parse( strim)
        steri=st(data = pathondata)
        if steri.is_valid():
            steri.save()
            data={'mas':'data created'}
            sdata=JSONRenderer().render(data)
            return HttpResponse(sdata)
        # data={'mas':'data not created'}
        sdata=JSONRenderer().render(steri.errors)
        return HttpResponse(sdata)
    if req.method == 'GET':
        data=req.body
        stetim=io.BytesIO(data)
        pythondata=JSONParser().parse(stetim)
        id = pythondata.get('id',None)
        if id is not None:
            stu =student.objects.get(id=id)
            sre=st(stu)
            jasdata=JSONRenderer().render(sre.data)
            return HttpResponse(jasdata)
        stu=student.objects.all()
        sre=st(stu,many=True)
        jasdata=JSONRenderer().render(sre.data)  
        return HttpResponse(jasdata)
    if req.method =='PUT':
        jesondata=req.body
        strim=io.BytesIO(jesondata)
        pytho=JSONParser().parse(strim)
        id=pytho.get('id')
        tu=student.objects.get(id=id)
        serr=st(tu, data=pytho,partial=True)
        # serr=st(tu, data=pytho) full update
        if serr.is_valid():
            serr.save()
            rees={'mes':'data update'}
            jasdata=JSONRenderer().render(rees)
            return HttpResponse(jasdata)
        jasdata=JSONRenderer().render(serr.errors)
        return HttpResponse(jasdata)
    rees={'mes':'data dfj'}
    jasdata=JSONRenderer().render(rees)
    return HttpResponse(jasdata)       
        
      

    
    
    
   
              

