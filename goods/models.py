# from django.db import models
#
# # Create your models here.
# from django.contrib.auth import get_user_model
# User = get_user_model()
#
#
# class Goods(models.Model):
#
#     """
#     upload_to：Specify the image upload location
#     %Y%m%d：Is the formatting of a date, which is eventually formatted as system time.
#     For example, if the picture was uploaded on December 5, 2018,
#     the picture will be saved in /media/avatar/2018205/
#     ImageField:  the ImageField field does not store the image itself, only the image's address.
#     Pillow: Remember to install the Pillow with the PIP instruction.
#
#     """
#     user = models.ForeignKey(User, verbose_name="用户")
#     order = models.ForeignKey(OrderInfo, verbose_name="订单信息")
#     goods = models.ForeignKey(Goods, verbose_name="商品")
#     add_time = models.DateTimeField(default=datetime.now,
#                                     verbose_name="添加时间")
#     avatar = models.ImageField(upload_to='avatar/%Y%m%d', blank=True)
#
#     class Meta:
#         verbose_name = "用户收藏"
#         verbose_name_plural = verbose_name
#         unique_together = ("uer", "goods")
#
#     def __str__(self):
#         return self.user.username
#
#
#
#
#
#
