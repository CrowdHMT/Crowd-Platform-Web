import json
import shutil, os, sys
import re
import socket
import pickle
import threading
from tabnanny import check

from django.conf import settings
from django.http import Http404, JsonResponse, StreamingHttpResponse
from django.utils.encoding import escape_uri_path
from rest_framework import status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView

from djangoProject.settings import SYSMODELDIA_ROOT, SYSMODELCODEDIA_ROOT
from djangoProject.settings import DOWNLOADFILEDIR_ROOT, UPLOADUSERMODEL_ROOT
from hmt.models import Device, Mission, ImageClassification
from hmt.serializers import DeviceSerializer, ImageClassificationSerializer

from hmt.models import SysModel, SysDeviceLatency
from hmt.serializers import SysModelSerializer, SysDeviceLatencySerializer

from operator import itemgetter
from pynvml import *

data_android = {"CPU_Arch": "armv7l", 
        "OS_Version": "Raspbian GNU/Linux 10", 
        "RAM_Total": 0, 
        "CPU_Use": "1.5", 
        "MEM_Use": 15.99888854,
        "DISK_Free": ""}

data_android = json.dumps(data_android)

class DeviceAndroid(APIView):
    
    global data_android
    
    def get(self, request): 
        
        return JsonResponse(json.loads(data_android))#json.load(data)就是一个json字符串反序列化为python对象
        #return JsonResponse(data)
            
    def post(self, request):
        
        data_android = request.body   #request.body就是获取http请求的内容,data是一个json格式的bytes对象

        # JsonResponse（）参数必须是字典对象，把其序列化为json格式，返回json格式的请求 如果参数不是Python对象，那么JsonResponse()将引发TypeError异常。
        return JsonResponse({"errorcode":0})