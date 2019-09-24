from rest_framework import viewsets


class ShoppingCartViewSet(viewsets.ModelViewSet):
    """
    购物车功能
    : params :list : 获取购物车详情
    : params : create : 加入购物车
    : params : delete : 删除购物记录
    购物车功能
    点击商品——"+"添加——1、购物车里出现商品 2、直接去购物车结算（商品、数量发生变化 最终价格 同时
    配送地址后台显示）
    后台逻辑：
    1、添加多次还是新增一条记录，有，则数量+1， 没有，则新增一条记录
    2、后台做加一减一操作，用同一个接口传递不同的参数？
    用到了mixin中的所有功能(增删查改)

    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classed = (JSONWwebTokenAuthentication,
                              SessionAuthentication)
    # queryset = shoppingcart.objects.all()

    serializer_class = ShopCartSerializer
    lookup_field = "goods_id"  # 传递一个商品进来

    def get_queryset(self):
        return shoppingcart.objects.filter(user=self.request.user)

    def create(self, validated_data):
        user = self.context["request"].user
        nums = validated_data["nums"]
        goods = validated_data["goods"]
        existed = shoppingcart.objects.filter(user=user, goods=goods)

        if existed:
            existed = existed[0]
            existed.nums += nums
            exists.save()



    # 重写udate方法
    def update(self, instance, validated_data):
        # 修改商品数量
        instance.nums = validated_data["nums"]
        instance.save()
        return instance


class OrderViewSet(mixins.ListModelViewSet. mixins.CreateModelMixin, mixins.DestoryModelMixin,
                   mixins.ViewSetGeneric.viewset):
    """订单管理"""
    # 订单不允许修改，不存在UpdateMixin
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authenticated_classes = (JSONWebTokenAuthentication,
                             SessionAuthentication)
    serializer_class = OrderSerializer


    def get_queryset(self):
        # 获取当前用户订单
        return OrderInfo.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer

    def generate_order_sn(self):
        # 当前时间userid+随机数
        # order_sn = "(time__str)(userid)(ranstr)".format(time__str = time.strftime(%Y%m%d%H%m%s),
         #           userid=self.context["request"], randstr = random_ins.randint(10, 99))"
        return order_sn

    def perform_create(self, serializer):
        order = serializer.save()
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            """生成订单"""
            order_goods = OrderGoods()
            order_goods.goods = shop_cart.goods
            order_goods.goods_num = shop_cart.nums
            order_goods.order = order
            order.save()
            shop_cart.delete()
            return order

    def validate(self, attrs):
        """断点调试"""
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
        Model = orderInfo
        fields = "__all__"






