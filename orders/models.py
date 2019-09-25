# from django.db import  models
# from django.contrib.auth import get_user_model
# User = get_user_model()
#
#
# class OrderInfo(models.Model):
#     ORDER_STATUS = (
#         ("success","成功"),
#         ("cancel", "取消"),
#         ("wait", "待支付"),
#     )
#     user = models.ForeignKey(User, verbose_name=u"用户")
#     order_sn = models.CharField()
#     trade_no = models.CharField() # 支付宝给的订单号
#     pay_status = models.CharField(choices=ORDER_STATUS)
#     # pay_time = models.DateTimeField()
#
#     # 用户信息
#     address = models.CharField()
#     signer_name = models.CharField()
#     signer_mobile = models.CharField()
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
#     # 订单和订单详情是一对多的关系
#     PAY_TYPE = (
#         ("alipay", "支付宝"),
#         ("wechat", "微信")
#     )
