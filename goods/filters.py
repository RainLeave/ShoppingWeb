class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(name="shopprice", lookuo_expr='gte')
    pricemax = django_filters.NumberFilter(name="shopprice", lookuo_expr='lte')
    top_category = django_filters.NumberFilter(nmethod='top_category_filter')


    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(Category_id=value)(Q(category_parent_Cate)))

    class Meta:
        model = Goods
        fields = ["pricemin", "pricemax", "is_hot"]

    