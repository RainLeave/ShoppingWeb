from .serializers import LeavingMessageSerializer, UserFavSerializer, UserFavDetailSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import JSONWebTokenAuthentication
from .models import UserFav
from utils.permissions import IsOwnerOrReadOnly

class LeavingMessageViewSet(mixins.ListModelMixin, mixins.DestoryModelMixin,
                            mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
        添加留言
    delete:
        删除留言
    """
    serializer_class = LeavingMessageSerializer # 配置Serializer
    def get_querysey(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)

# 用户收藏功能[7-03]
class UserFavViewSet1(mixins.CreateModelMixin,
                      mixins.ListModelMixin)
    permissions_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serialzier_class = UserFavSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    # 测试： 通过登录获取token，设置token放入header请求delete这个接口

# 用户收藏功能
from rest_framewokr.authentication import SessionAuthentication
from .models import UserFav
from utils.permissions import IsOwnerOrReadOnly
from .serializers import UserFavSerializer


class UserFavViewSet(mixins.CrateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin)
    """用户收藏功能"""
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserFavSerializer
    lookup_field = "goods_id"


    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    # 重写GenericAPIView的APIView中国的get_serializer_class(self)方法
    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer
        return UserFavSerializer

