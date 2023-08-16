from rest_framework.serializers import ModelSerializer
from favourite.models import Favourite
class FavouriteListCreateSerializer(ModelSerializer):
    class Meta:
        model=Favourite
        fields=['post','content',]

class FavouriteAPISerializer(ModelSerializer):
    class Meta:
        model=Favourite
        fields=['content']