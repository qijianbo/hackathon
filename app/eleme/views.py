#!/usr/bin/python
#-*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse 
from django.contrib.auth import authenticate
#from eleme.http import  Unauthorized,BadRequest,BadRequest1,Forbidden
try:
    import simplejson as json
except ImportError:
    import json
@csrf_exempt
def index (request):
    return HttpResponse('Hello_World.')
@csrf_exempt
def login (request):
    # try: 
    #     login()
    # except Exception,e: 
    #     return BadRequest()
    if request.method == 'POST':
        data = request.POST.get('data')
        try: 
            eval(data)
            return HttpResponse(status = 404)
        except Exception,e :
            return HttpResponse(
                json.dumps(
                {"code": 'MALFORMED_JSON',
                "message": '格式错误',}
                ),
                content_type='application/json',
                status = 400
                )
        username = request.POST.get('username','') 
        password = request.POST.get('password','') 
        user = authenticate(username = username, password = password)
        if user is not None:
            return HttpResponse(status = 502)
        else:
            return HttpResponse(
            json.dumps(
                {"code": 'USER_AUTH_FAIL',
                "message": '用户名或密码错误',}
            ),
            content_type='application/json',
            status = 403
        )
    else:
        return HttpResponse(
            json.dumps(
                {"code": 'MALFORMED_JSON',
                "message": '格式错误',}
            ),
            content_type='application/json',
            status = 400
        )
