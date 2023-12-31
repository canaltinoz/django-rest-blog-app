from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView
from rest_framework.mixins import DestroyModelMixin
from post.api.serializers import PostSerializer,PostUpdateSerializer
from post.models import Post
from post.api.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from post.api.paginations import PostPagination


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['title']
    pagination_class = PostPagination

    def get_queryset(self):
        queryset =Post.objects.filter(draft=False)
        return queryset

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView,DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)
class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


