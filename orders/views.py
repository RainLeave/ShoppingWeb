from django.views import View
from rest_framework.views import APIView

class OrderView(APIView):
    """
    文档注释
    基于类的视图，根据请求的方式(get、post、put、delete)调用对应的method
    :params ret: return error status code
    :params status: send the status code,eg,200,300,400,500
    """
    def get(self, request,*args,**kwargs):

        ret = {
            'code':1000,
            'msg':'xxx'
        }
        return HttpResponse(json.dumps(ret), status=200)

    def post(self, request, *args, **kwargs):
        return HttpResponse('创建订单')

    def put(self, request, *args, **kwargs):
        return HttpResponse('更新订单')

    def delete(self, request, *rags, **kwargs):
        return HttpResponse('删除 订单')