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
# from .serializers import SmsSerializer, UserRegSerializer, UserDetailSerializer
# from shoppingweb.settings import APIKEY
# from utils.yunpian import YunPian
# from .models import VerifyCode
# from rest_framework import permissions
# from django.http import JsonResponse
#
# User = get_user_model
#
#
# # 动态设置Serializer和permission获取用户信息
# # 重载Retrieve
# # 重用viewset
# class UserViewSet(createModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     """
#     用户
#     """
#     serializer_class = UserRegSerializer
#     queryset = User.objects.all()
#     authentication_classes = (JSONWebTokenAuthentication,)
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_seriaizer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = self.perform_crete(serializer)
#         re_dict = serializer.data
#         payload = jwt_payload_handler(user)
#         re_dict["token"] = jwt_encode_handler(payload)
#         re_dict["name"] = user.name if user.name else user.username
#         headers = self.get_success_headers(serializer.data)
#         return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
#
#     def get_object(self):
#         return self.request.user
#
#     def perform_create(self, serializer):
#         return serializer.save()
#
#     def get_permission(self):
#         if self.action == "retrieve":
#             return [permissions.IsAuthenticated()]
#
#         elif self.action == "create":
#             return []
#         return []
#
#     def get_serializer_class(self):
#         if self.action == "retrieve":
#             return UserDetailSerializer
#         elif self.action == "create":
#             return UserRegSerializer
#         return []

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


# Just for test
# 限制用户访问请求方式的装饰器：@require_http_methods(["GET"]) 表示只允许使用GET的method来访问视图
# @require_http_methods(["GET"]) means that only methods of GET are allowed to access views
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


def test(request):
    return JsonResponse({"status": 0, "message": "This is Django Message！"})


from django.core.serializers import serialize
# import importlib
# importlib.reload(sys)
from django.core.serializers.json import DjangoJSONEncoder


def test_book(request):
    if request.method == "GET":
        # db = serialize('json', Book.objects.all(), cls=LazyEncoder)
        # print(type(db))
        # db = serialize('json', Book.objects.all())
        # db1 = Book.objects.all()
        # db = json.dumps(list(db1),  cls=DjangoJSONEncoder)
        # db = Book.objects.filter(book_name='小王子')
        db = Book.objects.all()
        # db = i for i in db
        # print(db)
        db = [i.book_name for i in db]
        print(db)
        return JsonResponse({'status': 0, 'data': db})
    else:
        return JsonResponse({'status':1, 'message': 'You need GET method'})