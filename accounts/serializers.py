# 定义一个User Detail的Serializer

class UserDetailSerializer(serializers.ModelSerialzier):
    """
    用户详情序列化类
    """
    class Meta:
        Model = User
        fields = ("name", "gender", "birthday", "email", "mobile")

