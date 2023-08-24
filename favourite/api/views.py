from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from favourite.models import Favourite
from favourite.api.serializers import FavouriteListCreateSerializer,FavouriteAPISerializer
from rest_framework import serializers
from favourite.api.paginations import FavouritePagination
from favourite.api.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
class FavouriteListCreateAPIView(ListCreateAPIView):
    serializer_class = FavouriteListCreateSerializer
    pagination_class = FavouritePagination
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def validate(self,attrs):
        queryset=Favourite.objects.filter(post=attrs['post'],user=attrs['user'])
        if queryset.exists():
            raise serializers.ValidationError('Zaten favorilere eklendi.')
        return attrs

class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    permission_classes = [IsOwner]
    lookup_field = 'pk'