# from django.db import models
# from django.contrib.auth import get_user_model
# User = get_user_model()
#
# # 用户操作(留言、收藏、信息)
# class UserFav(models.Model):
#     user = models.ForeignKey(User, verbose_name=u"用户")
#     goods = models.ForeignKey(Goods)
#     add_time = models.DateTimeField(auto=now)
#
#     class Meta:
#         verbose_name = "用户收藏"
#
#     def __str__(self):
#         return self.user.name
#
# class UserLeavingMessage(models.Model):
#     MESSAGE_CHOICES = (
#         (1, "留言"),
#         (2, "投诉"),
#         (3, "咨询"),
#         (4, "售后"),
#         (5, "求购"),
#     )
#     # 用户留言
#     user = models.ForeignKey(User, verbose_name=u"用户")
#     msg_type = models.InterField(default=1, choices=MESSAGE_CHOICES,
#                                  help_text=u"留言类型:1(留言), 2(投诉), 2（询问), 4(售后), 5(求购)")
#     subject = models.CharField(max_length=100, default=" ", verbose_name="主题")
#     # msg_type = models.CharField()
#     message = models.TextField(default=" ",
#                                verbose_name=u"留言内容")
#     addt_time = models.DateTimeField(default=datetiem.now,
#                                      verbose_name=u"添加时间")
#     file = models.FileField(upload_to="message/images", verbose_name=u"上传的文件")
#
#     class Meta:
#         verbose_name = "用户留言"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.subject
#
#
# class UserAddress(models.Model):
#     user = models.ForeignKey(User, verbose_name=u"用户")
#     address = models.CharField()
#     signer_name = models.CharField()
#     signer_mobile = models.CharField()
#     add_time = models.DateTimeField(auto=now)
#
#     class Meta:
#         verbose_name = "用户地址"
#
#     def __str__(self):
#         return self.address
#
