from rest_framework import serializers
from foods.models import Foods
# from ...foods.models import Foods


class FoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = '__all__'

class CategorySerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    parent = serializers.IntegerField(required=False)
    slug = serializers.CharField(required=False)


