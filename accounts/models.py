# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


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

