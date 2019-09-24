from restframework import serializers


class ShopCartSerializer(serializers.Serializer):
    """
    TODO:暂时没有
    """
    # 映射model中的字段
    user = serializers.HiddenField(default=serializers.CurrentUserFault)
    numd = serializers.IntegerField(required=True, min_value=1, label="数量",
                                    error_messages={
                                        "min_value":"商品数量不能小于......",
                                        "required":"请选择购买数量"

                                    })
    goods = serializers.PrimiaryKeyRelatedField(required=True, queryset=Goods.object.all())

    def create(self, validated_data):
        """
        这个方法：
        做过valitdated后处理过的数据，不需要再做字符串转化
        :param validated_data:
        :return: boolean
        """
        # 获取当前用户
        # Q: 为什么从context中获取
        user = self.context["request"].user
        nums = validated_data["nums"]
        goods = validated_data["goods"]
        existed = ShoppingCart.objects.filter(user=user, goods=goods)

        if existed:
            existed = existed[0]
            existed.nums += num
            existed.save()
        else:
            ShoppingCarts.objects.create(**validated_data)
        return existed


class OrderSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    pay_status = serializers.CharField(read_only=True) # 只读不写

    def generate_order_sn(self):
        # 当前时间+userid+随机数
        from random import Random
        random_ins = Random()
        # order_sn = "(time_str){userid}(transtr)".format(time_str=time.strftime(%Y%m%d%H%m%s))
        return order_sn


class OderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True)

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    related_name = "goods"

    class Meta:
        model = OrderInfo
        fields = "__all__"
    goods = GoodSerializer(many=True)  # 外键通过many来获取
