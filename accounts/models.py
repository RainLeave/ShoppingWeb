# from django.db import models
#
#
# class UserProfile(AbstractUser):
#     """
#     用户
#     """
#     name = models.CharField(max_length=30, null=True, blank=True, verbose_name=u"姓名")
#     birthday = models.DateField(null=True, blank=True, verbose_name=u"出生年月")
#     gender = models.CharField(max_length = 6, choices =(('male', u"男"), 'female', "女"))
#     mobile = models.CharField(null=True, blank=True, verbose_name=u"手机号码")
#     email = models.EmailField(max_length=100, null=True, blank=True, verbose_name=u"邮箱")
#
#     class Meta:
#         verbose_name = "用户"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.username
#
#


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class Book(models.Model):
    """
    定义了一个Book类，用于显示书名book_name
    未指定主键，系统会自动添加
    :params book_ame: str
    :params date_public: str
    :rtype :str
    """
    book_name = models.CharField(max_length=50, default='', null=True)
    date_public = models.DateTimeField(
        _('date published'),
        default=timezone.now
    )

    # __str__函数和__unicode__函数对比
    def __str__(self):
        return self.book_name

