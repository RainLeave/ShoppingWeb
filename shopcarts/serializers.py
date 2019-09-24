# -*- coding: utf-8 -*-
__author__ = "sky"

from restframework import serializers


class ShopCartSerializer(serializers.Seralizer):
    # def create(self, validated_data):
    """
    下面的方法并未直接重载，而是参照写出来的验证方法
    """

    def create(self, request, *args, **keargs):
        """
        *args: 可变参数 后面也必须是关键词参数
        **kwargs: 可变关键词参数 位于参数列表的最后
        self: 表示这是个类的方法
        面向对象编程中，类中定义的方法区别于面向函数编程的一点在于，
        第一个参数必须是self参数
        Q: 为什么不用ModelSerializer，使用Serializer
        A；代码分离性好 文档不缺失 但是缺点在于验证出现无法通过
        只能自己做验证
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response(serializer.data,
                    status = status.HTTP_201_CREATED)
                    # headers = )
    def perform_create(self, serializer):
        # 如果前面发生异常报错，在下面的方法无法调用
        serializer.save()



