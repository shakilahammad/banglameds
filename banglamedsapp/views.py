# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
import django_filters
from rest_framework import viewsets, filters
#from rest_framework.decorators import detail_route, list_route
from rest_framework.views import APIView
import os
from rest_framework.response import Response
from datetime import datetime
from .models import *
from rest_framework.reverse import reverse
from .serializer import RegisteredStgSerializer, DistrictSerializer
from rest_framework.renderers import JSONRenderer
from django.core.files.storage import FileSystemStorage
import json
import datetime
import requests
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
from django.http import JsonResponse
from django.core import serializers
from time import sleep

from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
#from django.core import serializers
from django.core.serializers import serialize
from functools import reduce
from random import randint
from django.db import DatabaseError, transaction
import http.client, urllib.request, urllib.parse, urllib.error, base64

from requests_oauthlib import OAuth1Session
from django.http import JsonResponse



class AllProduct(viewsets.ModelViewSet):
    #queryset = District.objects.all()
    # queryset = RegisteredUser.objects.all()

    # role_class = RegisteredStgSerializer
    # queryset = RegisteredUser.objects.all()
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    role_class = DistrictSerializer

    # Endpoint to receive image from mobile app

    def create(self, request):
        response = {'StatusCode': '200', 'StatusMessage': 'resend'}
        return Response(response, content_type="application/json")

    def list(self, request):
        # queryset = District.objects.all().values('Id', 'DistrictName').using('YamahaBooking')
        # data = json.dumps(list(queryset))

        twitter = OAuth1Session('1cb615ef0b50b640324bb7e614551f7b',
                                client_secret='edf2e5500bd06bdcf0a48182236917af',
                                resource_owner_key='bfddd465b6ea96755e5b170c7dc5adec',
                                resource_owner_secret='d4b2655c7355faa644dd9dcf20948b57')
        url = 'http://staging.banglameds.com.bd/api/rest/productlist?name=napa&page='
        r = twitter.get(url)
        #print("=====" + str(r.json()))
        msg = "1"

        return Response(r.json(), content_type="application/json")
#viewsets.ModelViewSet
class AllDistrict(viewsets.ModelViewSet):
    queryset = District.objects.all()
    #queryset = RegisteredUser.objects.all()
    serializer_class = DistrictSerializer
    role_class = DistrictSerializer

    def get_serializer_class(self):
        return self.role_class

    def list(self, request):
        # queryset = District.objects.all().values('Id', 'DistrictName').using('YamahaBooking')
        # data = json.dumps(list(queryset))

        twitter = OAuth1Session('1cb615ef0b50b640324bb7e614551f7b',
                                client_secret='edf2e5500bd06bdcf0a48182236917af',
                                resource_owner_key='bfddd465b6ea96755e5b170c7dc5adec',
                                resource_owner_secret='d4b2655c7355faa644dd9dcf20948b57')
        url = 'http://staging.banglameds.com.bd/api/rest/districts'
        r = twitter.get(url)
        print("=====" + str(r.json()))
        msg = "1"
        return JsonResponse(str(r.json()), safe=False)
        #return Response(r.json(), content_type="application/json")

class Areas(viewsets.ModelViewSet):
    #queryset = District.objects.all()
    # queryset = RegisteredUser.objects.all()
    # role_class = RegisteredStgSerializer

    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    role_class = DistrictSerializer

    def list(self, request):
        aCode = request.GET.get('AreaCode')
        twitter = OAuth1Session('1cb615ef0b50b640324bb7e614551f7b',
                                client_secret='edf2e5500bd06bdcf0a48182236917af',
                                resource_owner_key='bfddd465b6ea96755e5b170c7dc5adec',
                                resource_owner_secret='d4b2655c7355faa644dd9dcf20948b57')
        url = 'http://staging.banglameds.com.bd/api/rest/areas/'+str(aCode)
        r = twitter.get(url)
        #print("=====" + str(r.json()))
        msg = "1"
        return Response(r.json(), content_type="application/json")

class Orderstatus(viewsets.ModelViewSet):
    #queryset = District.objects.all()
    #role_class = RegisteredStgSerializer
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    role_class = DistrictSerializer

    def list(self, request):
        orderCode = request.GET.get('OrderCode')
        twitter = OAuth1Session('1cb615ef0b50b640324bb7e614551f7b',
                                client_secret='edf2e5500bd06bdcf0a48182236917af',
                                resource_owner_key='bfddd465b6ea96755e5b170c7dc5adec',
                                resource_owner_secret='d4b2655c7355faa644dd9dcf20948b57')
        url = 'http://staging.banglameds.com.bd/api/rest/orderstatus/'+str(orderCode)
        r = twitter.get(url)
        #print("=====" + str(r.json()))
        msg = "1"
        return Response(r.json(), content_type="application/json")

class OrderList(viewsets.ModelViewSet):
    queryset = District.objects.all()
    role_class = RegisteredStgSerializer

    def list(self, request):
        twitter = OAuth1Session('1cb615ef0b50b640324bb7e614551f7b',
                                client_secret='edf2e5500bd06bdcf0a48182236917af',
                                resource_owner_key='bfddd465b6ea96755e5b170c7dc5adec',
                                resource_owner_secret='d4b2655c7355faa644dd9dcf20948b57')
        url = 'http://staging.banglameds.com.bd/api/rest/orderlist'
        r = twitter.get(url)
        #print("=====" + str(r.json()))
        msg = "1"
        return Response(r.json(), content_type="application/json")

class Order(viewsets.ModelViewSet):
    queryset = District.objects.all()
    role_class = RegisteredStgSerializer

    def list(self, request):
        orderCode = request.GET.get('OrderCode')
        twitter = OAuth1Session('1cb615ef0b50b640324bb7e614551f7b',
                                client_secret='edf2e5500bd06bdcf0a48182236917af',
                                resource_owner_key='bfddd465b6ea96755e5b170c7dc5adec',
                                resource_owner_secret='d4b2655c7355faa644dd9dcf20948b57')
        url = 'http://staging.banglameds.com.bd/api/rest/order/'+str(orderCode)
        r = twitter.get(url)
        #print("=====" + str(r.json()))
        msg = "1"
        return Response(r.json(), content_type="application/json")