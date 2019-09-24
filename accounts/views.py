from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from rest_framework.views import APIView

# test
from .models import Book


class UserLoginView(APIView):
    '''
    用户登录认证
    '''
    pass

    def post(self, request, *args, **kwargs):
        pass


@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# # 动态设置Serializer和permission获取用户信息
# from django.shortcuts import render
# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
# from django.db.models import Q
# from restf_framework.mixins import CreateModelMixin
# from restf_framework import mixins
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from random import choice
# from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
# from .serializers import SmsSerializer, UserRegSerializer
# from shoppingweb.settings import APIKEY
# from utils.yunpian import YunPian
# from .models import VerifyCode
#
#
# User = get_user_model
