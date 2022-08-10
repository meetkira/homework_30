from rest_framework import serializers

from ads.models import Ad


class AdSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='first_name'
    )
    '''image = serializers.SlugRelatedField(
        read_only=True,
        slug_field='url',
        allow_empty=True,
    )'''

    class Meta:
        model = Ad
        fields = "__all__"
