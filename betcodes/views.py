from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
import logging

from betcodes.models import BetCode, FootballTeam, BookCodeInfo, Post, Comment, Continent, Country, Competition
from betcodes.serializers import BetCodeSerializer, FootballTeamSerializer, BookCodeInfoSerializer, CommentSerializer, PostSerializer, CompetitionSerializer, CountrySerializer, ContinentSerializer


logger = logging.getLogger(__name__)


class BetCodeViewSet(ModelViewSet):
    queryset = BetCode.objects.all()
    serializer_class = BetCodeSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


class BookCodeInfoViewSet(ModelViewSet):
    queryset = BookCodeInfo.objects.all()
    serializer_class = BookCodeInfoSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related('user', 'comments').all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user_id'] = self.request.user
        return context


class ProfilePostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.prefetch_related('user', 'comments').filter(user_id=self.request.user.id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user_id'] = self.request.user
        logger.info('self.kwargs2')
        return context


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk'], 'user_id': self.request.user}


# class LikesViewSet(ModelViewSet):
#     serializer_class = LikeSerializer

#     def get_queryset(self):
#         return Likes.objects.filter(post_id=self.kwargs['post_pk'])

#     def get_serializer_context(self):
#         return {'post_id': self.kwargs['post_pk'], 'user_id': self.request.user}


class ContinentViewSet(ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    permission_classes = [IsAdminUser]

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]

class CompetitionViewSet(ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [IsAdminUser]

class FootballTeamViewSet(ModelViewSet):
    queryset = FootballTeam.objects.all()
    serializer_class = FootballTeamSerializer
    permission_classes = [IsAdminUser]
