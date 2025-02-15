from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.name")  # owner는 읽기 전용 (이름 출력)

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["owner", "created_at", "updated_at"]
