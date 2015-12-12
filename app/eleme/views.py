#coding:utf-8
#from django.shortcuts import render
from django.http import HttpResponse
#from Controller
#from django.contrib.auth import authenticate
#from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
#from django.contrib.auth import get_user_model
#from eleme.tokens import token_generator
from django.contrib import auth
#from eleme.models import user
from eleme.http import JsonError,JsonResponseBadRequest
#from app.reverse_models import Food, User
#try:
#    import simplejson as json
#except ImportError:
 #   import json
#try:
#    from django.contrib.auth import get_user_model
#except ImportError: # Django < 1.5
#    from django.contrib.auth.models import User
#else:
 #   User = get_user_model()
#def index(request):
#	users = user.objects.all()
#   return HttpResponse("HttpResponse")
	
#	return HttpResponse("HttpResponse")
# Create your views here.
#@csfr_exempt
def login(request):
    if  request.method == 'POST':
        request.session.delete_test_cookie()
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        return HttpResponse(status=200)
#        return HttpResponse(username)
#        if username and password:
        user = auth.authenticate(username=username, password=password)

 #           if user:
 #               TOKEN_CHECK_ACTIVE_USER = getattr(settings, "TOKEN_CHECK_ACTIVE_USER", False)

        if user is not None:    #and user.is_active:
            auth.login(request,user)
            return HttpResponse (status=200)
                 #   return JsonResponse(status=200)
 #                  data = {
 #                       "user_id": id,
 #                       "username": username,
 #                       "access_token": token_generator.make_token(user),
 #                   }
 #               return JsonResponse(data)
 #           else:
 #               return JsonError(code='USER_AUTH_FAIL',error_string='用户名或密码错误')#status=403
 #       else:
 #           return JsonError(code='EMPTY_REQUEST',error_string='请求体为空')#status=400
 #   else:
#        return HttpResponse(status=400)
#        return JsonError(code='MALFORMED_JSON',error_string
        else:
            return HttpResponse (status=403)
    else:
        return JsonResponseBadRequest("error_string")

    











