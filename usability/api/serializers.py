from rest_framework import serializers

from usability.models import Subscriber, AdminMessage, FavoriteProduct


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = 'email',


class AdminMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminMessage
        fields = 'name', 'email', 'message'
        read_only_fields = 'ip', 'created'

    def create(self, validated_data):
        """
        Сохраним ip адрес написавшего
        """
        request = self.context.get('request')
        if request:
            validated_data['ip'] = request.META.get('REMOTE_ADDR')
        return AdminMessage.objects.create(**validated_data)


class ShortFavoriteProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FavoriteProduct
        fields = 'user', 'product'


