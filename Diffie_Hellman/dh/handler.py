from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import api
import pathlib

@csrf_exempt
def gen_p_handler(req):
    param = req.POST
    p = api.gen_p()
    return JsonResponse({'p': p})

@csrf_exempt
def gen_a_handler(req):
    param = req.POST
    a = int(api.gen_a(int(param['p'])))
    return JsonResponse({'a': a})

@csrf_exempt
def show_encode_handler(req):
    param = req.POST
    plain = param['plain']
    key = param['key']
    encode = api.show_encode(plain, key)
    encode = encode.decode("utf-8") 
    return JsonResponse({'encode': encode})

@csrf_exempt
def show_decode_handler(req):
    param = req.POST
    cipher = param['cipher']
    key = param['key']
    dec = api.show_decode(cipher, key)
    dec = dec.decode("utf-8") 
    return JsonResponse({'dec': dec})