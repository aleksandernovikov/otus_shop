from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import SubscriberSerializer, AdminMessageSerializer
from ..models import Subscriber, AdminMessage


class SubscriberViewSet(CreateModelMixin, GenericViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class AdminMessageViewSet(CreateModelMixin, GenericViewSet):
    queryset = AdminMessage.objects.all()
    serializer_class = AdminMessageSerializer
