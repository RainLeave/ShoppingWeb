class GoodsListViewSet(mixins.ListModelmixin,
                       mixins.RetrieveModelmixin):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    paginationn_class = GoodsPagination
    # authentication_classes = (TokenAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('add_num', 'shop_price')

