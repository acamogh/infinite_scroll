
from rest_framework import serializers,pagination
from .models import Theme

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'theme_name')

# class PaginatedUserSerializer(pagination.PaginationSerializer):
#
#     class Meta:
#         object_serializer_class = ThemeSerializer