from django.db import models


class ShoppingCart(models.Model):
    """购物车模型"""

    # user = models.ForeignKey(User, verbose_name=u"用户")
    # goods = models.ForeignKey(Goods, verbose_name=u"商品")
    nums = models.IntegerField(default=0, verbose_name=u"购买数量")
    # add_time = models.DateTimeField(default=dateTime.now,
                                    # verbose_name=u"添加时间")
    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        # unique_together = ("user", "good")  # 构成唯一联合索引

    def __str__(self):
        return "%s%d".format(self.goods.name, self.nums)

