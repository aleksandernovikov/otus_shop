from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import ProductFilter
from .serializers import DefaultCartProductSerializer, ShortCartProductSerializer, ShortProductSerializer
from ..models.cart import CartProduct
from ..models.product import Product


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ShortProductSerializer
    filter_backends = filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend
    filterset_class = ProductFilter
    search_fields = 'title', 'description', 'price',
    ordering_fields = 'sort_order', 'price',


class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = DefaultCartProductSerializer

    permission_classes = (IsAuthenticated,)

    action_serializers = {
        'create': ShortCartProductSerializer,
        'destroy': ShortCartProductSerializer,
    }

    def get_serializer_class(self):
        if self.action in self.action_serializers:
            return self.action_serializers[self.action]
        return self.serializer_class

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        чтобы при добавлении продукта, учитывалать существующую корзину
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        already_added = self.get_queryset().filter(
            product__id=serializer.data.get('product')
        )

        if already_added.exists():
            already_added.update(count=F('count') + serializer.data.get('count'))
        else:
            super().create(request, *args, **kwargs)

        return self.cart_products_count(request, set_status=status.HTTP_201_CREATED)

    @action(methods=['GET'], detail=False, url_path='count', url_name='cart-products-count')
    def cart_products_count(self, request, set_status=status.HTTP_200_OK):
        """
        Количество продуктов в корзине
        """
        cart = CartProduct.cart_products_minimal(request.user)
        data = {
            'count': cart.get('count', 0),
            'total': cart.get('total', 0)
        }
        return Response(data, status=set_status)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        # with 204 status code - no data
        return self.cart_products_count(request)
