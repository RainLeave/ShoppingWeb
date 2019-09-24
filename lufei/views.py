from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions
import json


class MyAuthentication(object):
    """
    URL认证成功才可以访问，认证成功是基于传过来的token
    认证成功返回一个元组
    没有认证成功，则报错
    """
    def authenticate(self, request):
        # request.py中的request类下的user方法中调用的request方法
        # 通过request可以获取用户请求的数据
        token = request._request.GET["token"]  # 获取请求的值，request._request表示原生的request
        if not token: # 如果token不存在，表示并未传，意味着用户未登录，抛出异常
            raise exceptions.AuthenticatedField("用户认证失败")
        return ('alex', None)

    # 注意：我这里是正常执行，并未提示需要token
    # 对比视频
    def authenticate_header(self, val):
        pass

class DogView(APIView):   # django的view
    # 获取BasicAuthentication类的对象
    authentication_classes = [BasicAuthentication,]

    def get(self, request, *args, **kwargs):

        ret = {
            'code': 1000,
            'msg': 'xxx'
        }
        return HttpResponse(json.dumps(ret), status=201)

    def post(self, request, *args, **kwargs):
        self.dispatch
        return HttpResponse("创建Dog")

    def put(self, request, *args, **kwargs):
        return HttpResponse("更新Dog")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("删除Dog")


"""
总结：正常是将判断用户是否登录写在DogView视图中
但是这里通过Myauthentication来实现了
如果带token，程序执行继续往下走
"""

# 对原生的request进行加工(丰富了一些功能)
# Request(request, parsers=self.get_parser(), authenticators=self.get_authenticators()
# negatitor）
# request(原生request, [BasicAuthentication对象,])

# 获取原生request: request._request
# 获取认证类的对象： request.authenticators

# 1、封装request
# 2、认证
# 3、
# 4、实现认证
# 5、找user方法（fron restframework import Request）
# 获取认证对象，进行一步步的认证
# 6、循环所有的认证对象