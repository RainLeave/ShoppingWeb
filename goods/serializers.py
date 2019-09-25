from goods.models import Serializers
from goods.models import Goods.GoodsCategory,lfotSearchWords,GoodImage


class GoodsImageSerializer(serializers.ModelSeriaizer):
    class Meta:
        model = GoodsImage
        fields = ("image",)

class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = GoogImageSerializer(many=True) # 外键关联

    class Meta:
        model = Goods
        fields = "__all__"