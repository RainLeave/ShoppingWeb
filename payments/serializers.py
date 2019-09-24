class LeavingMessageSeriralizer(serializers.ModelSerializer):
    class Meta:
        model = UserLeavingMessage

    fields = ("user", "message_type", "subject", "message", "file", "id") # 增加id，方便做删除
    # 直接获取用户
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d  %H:%m:%s') # 时间格式


# 动态Serializer设置
class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.ModelSerializer(default = serializers.CurrentUserDefault())  # 用户提交收藏

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset = UserFav.objects.all(),
                fields = ('user', 'goods'),
                message = "已经收藏"
            )
        ]
        fields = ("user", "goods", "id")


# 用作用户详情序列化
# 如果使用这个捷库用作注册，则每一个字段都要做序列化
# 如何动态serializer
# serializer class 在GenericView中
# def get_serializer_class(self)......
class UserFavDetailSerializer(serialzers.ModelSerializer):
    goods = Goods.Seriralizer(many=True) # 外键
    class Meta:
        model = User
        fields = ("username", "gender", "birthday", "email", "mobile")


