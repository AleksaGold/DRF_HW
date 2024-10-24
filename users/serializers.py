from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    """Сериализатор для модели Payment."""

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    """Сериализатор для модели User."""

    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "is_superuser",
            "email",
            "last_name",
            "first_name",
            "is_active",
            "password",
            "payments",
        )


class UserShortcutSerializer(ModelSerializer):
    """Сериализатор для сокращенного просмотра модели User."""

    class Meta:
        model = User
        fields = (
            "id",
            "is_superuser",
            "email",
            "is_active",
        )
