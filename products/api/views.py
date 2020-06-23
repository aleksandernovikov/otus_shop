from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import DefaultCartProductSerializer, ShortCartProductSerializer
from ..models.cart import CartProduct


class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = DefaultCartProductSerializer

    action_serializers = {
        'create': ShortCartProductSerializer,
        'destroy': ShortCartProductSerializer,
    }

    def get_serializer_class(self):
        if self.action in self.action_serializers:
            return self.action_serializers[self.action]
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        # при добавлении продукта, учитывалать существующую корзину
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        already_added = CartProduct.objects.filter(
            owner=request.user,
            product__id=serializer.data.get('product')
        )

        if already_added.exists():
            already_added.update(count=F('count') + serializer.data.get('count'))
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return super().create(request, *args, **kwargs)

    @action(methods=['GET'], detail=False, url_path='count')
    def cart_products_count(self):
        pass
    # def destroy(self, request, *args, **kwargs):
    #     print('destroy')
    #     return super().destroy(request, *args, **kwargs)
