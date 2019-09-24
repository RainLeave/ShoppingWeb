from django.db import Model


class OrderInfo(models.Model):
    """订单管理"""
    ORDER_STATUS = (
        ("success", "成功"),
        ("cancel", "取消"),
        ("wait", "待支付"),
    )
    user = models.ForeignKey(User, verbose_name="用户")
    order_sn = models.CharField(max_length=30, null=True, blank=True,
                                unique=True)
    trade_no = models.CharField(max_length=100, null=True, blank=True,
                                unique=True)
    pay_status = models.CharField(max_length=200, verbose_name="订单留言")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")

    # 用户信息
    address = models.CharField(max_length=100, default=" ",verbose_name="收货地址")
    singer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
    singer_mobile = models.CharField(max_length=11, verbose_ame="联系电话")
    add_time = models.DateTimField(dafaule=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


    class OrderGoods(models.Model):
        """订单商品详情"""
        order = models.ForeignKey(OrderInfo, verbose_name="订单信息")
        goods = models.ForeignKey(Goods, verbose_name="商品")
        goods_num = models.IntegerField(default=0, verbose_name="商品数量")
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

        class Meta:
            verbose_name = "订单商品"
            verbose_name_plural = verbose_name

        def __str__(self):
            return str(self.order.order_sn)