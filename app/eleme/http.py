"""JSON helper functions"""
try:
    import simplejson as json
except ImportError:
    import json

from django.http import HttpResponse


def JsonResponse(data, dump=True):#status=200):
 #   try:
 #       data['errors']
 #   except KeyError:
 #       data['success'] = True
 #   except TypeError:
 #       pass

    return HttpResponse(
        json.dumps(data) if dump else data,
        content_type='application/json',
#        status=status,
    )


def JsonError(code,message):#,status=200):
    data = {
        "code": code,
        "message": message,
       }
    return JSONResponse(data)

def Unauthorized():
    return JsonError(code='INVALID_ACCESS_TOKEN',message='无效的令牌',status=401)

def BadRequest1():
    return JsonError(code='EMPTY_REQUEST',message='请求体为空',status=400)
def BadRequest(httpcode):
    return JsonError(code='MALFORMED_JSON',message='格式错误',status=httpcode)
def Forbidden():
    return JsonError(code='USER_AUTH_FAIL',message='用户名或密码错误',status=403)
#def JsonResponseBadRequest(error_string):
#    return JsonError(error_string, status=400)


#def JsonResponseUnauthorized(error_string):
#    return JsonError(error_string, status=401)


#def JsonResponseForbidden(error_string):
#    return JsonError(error_string, status=403)


#def JsonResponseNotFound(error_string):
#    return JsonError(error_string, status=404)


#def JsonResponseNotAllowed(error_string):
#    return JsonError(error_string, status=405)


#def JsonResponseNotAcceptable(error_string):
#    return JsonError(error_string, status=406)


# For backwards compatability purposes
JSONResponse = JsonResponse
JSONError = JsonError
