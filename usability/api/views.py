from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import SubscriberSerializer, AdminMessageSerializer, ShortFavoriteProductSerializer
from ..models import Subscriber, AdminMessage, FavoriteProduct


class SubscriberViewSet(CreateModelMixin, GenericViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class AdminMessageViewSet(CreateModelMixin, GenericViewSet):
    queryset = AdminMessage.objects.all()
    serializer_class = AdminMessageSerializer


class FavoriteProductViewSet(viewsets.ModelViewSet):
    queryset = FavoriteProduct.objects.all()
    serializer_class = ShortFavoriteProductSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        qs = self.get_queryset().filter(user=request.user)

        already_added = qs.filter(
            product=serializer.data.get('product')
        )

        if already_added.exists():
            already_added.delete()
        else:
            super().create(request, *args, **kwargs)
        headers = self.get_success_headers(serializer.data)
        return Response({'count': qs.count()}, status=status.HTTP_200_OK, headers=headers)
