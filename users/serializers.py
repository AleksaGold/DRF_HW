from rest_framework.serializers import ModelSerializer

from users.models import Payment


class PaymentSerializer(ModelSerializer):
    """Сериализатор для модели Payment"""

    class Meta:
        model = Payment
        fields = "__all__"
