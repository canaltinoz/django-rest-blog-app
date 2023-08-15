from rest_framework.serializers import ModelSerializer,SerializerMethodField
from comment.models import Comment
from rest_framework import serializers
class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model=Comment
        exclude=['created','user',]

        def validate(self,attrs):
            if(attrs['parent']):
                if attrs['parent'].post != attrs['post']:
                    raise serializers.ValidationError('validation error')
            return attrs
class CommentListSerializer(ModelSerializer):
    replies=SerializerMethodField()
    class Meta:
        model=Comment
        fields='__all__'
    def get_replies(self,obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data

class CommentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields=['content']
