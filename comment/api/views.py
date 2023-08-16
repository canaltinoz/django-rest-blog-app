from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin
from comment.api.serializers import CommentCreateSerializer,CommentListSerializer,CommentDeleteUpdateSerializer
from comment.models import Comment
from comment.api.permissions import IsOwner

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    def get_queryset(self):
        return Comment.objects.filter(parent=None)

class CommentUpdateAPIView(UpdateAPIView,RetrieveAPIView,DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)
