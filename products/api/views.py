from decimal import Decimal

from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import DefaultCartProductSerializer, ShortCartProductSerializer
from ..models.cart import CartProduct


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

        return self.cart_products_count(request)

    @action(methods=['GET'], detail=False, url_path='count', url_name='cart-products-count')
    def cart_products_count(self, request):
        """
        Количество продуктов в корзине
        :param request:
        :return:
        """
        cart = CartProduct.cart_products_minimal(request.user)
        data = {
            'count': cart.get('count', 0),
            'total': cart.get('total', 0)
        }
        return Response(data, status=status.HTTP_200_OK)
