from django.http import HttpResponse
import json


class GoodListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        for good in goods:
            json_dict = {}
            json_dict["name"] = good.name
            json_dict["category"] = good.category.name
            json_dict["market_price"] = good.market_price
            json_dict["add_time"] = goos.add_time
            json_dict.append(json_dict)
        return HttpResponse(json.dums(json_list), content_type="application/json")

    # 方法二
    from django.forms.models import mode_to_dict
    for good in goods:
        json_dict = model_to_dict(good)
        json_list.append(json_dict)
    import json
    from django.core import serializers
    json_data = serializers("json", goods)
    json_data = json.loads(json_data)


