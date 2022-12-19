from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsSafeMethodOrIsAuthor
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from api.utils import get_post
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsSafeMethodOrIsAuthor, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsSafeMethodOrIsAuthor, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_post(self),
        )

    def get_queryset(self):
        post = get_post(self)
        return post.comments.select_related('author')
