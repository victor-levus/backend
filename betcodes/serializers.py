from rest_framework import serializers

from betcodes.models import BetCode, BookCodeInfo, FootballClub, Post, Comment


class BetCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BetCode
        fields = ['id', 'home_team', 'away_team', 'bet', 'odd', 'ht_home_score',
                  'ht_away_score', 'ft_home_score', 'ft_away_score', 'bet_status', 'match_time']


class BookCodeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCodeInfo
        fields = ['book_code', 'total_odd', 'ticket_date']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'description', 'parent', 'replies', 'created_at']

    def create(self, validated_data):
        post_id = self.context['post_id']
        user_id = self.context['user_id']
        return Comment.objects.create(post_id=post_id, user_id=user_id.id, **validated_data)
    
    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return None

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user_id = self.context['user_id']
        return Post.objects.create(user_id=user_id.id, **validated_data)

    class Meta:
        model = Post
        fields = ['id', 'user', 'description', 'placed_at', 'comments']


class FootballClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballClub
        fields = ['club_name', 'country',
                  'continent', 'domestic_league', 'logo']



# class LikeSerializer(serializers.ModelSerializer):
#     user = serializers.CharField(read_only=True)

#     class Meta:
#         model = Likes
#         fields = ['id', 'user', 'likes', 'placed_at']

#     def create(self, validated_data):
#         post_id = self.context['post_id']
#         user_id = self.context['user_id']
#         verify_like = Likes.objects.filter(user_id=user_id.id)

    # if (verify_like):
    #     return
    # else:
    #     return Likes.objects.create(post_id=post_id, user_id=user_id.id, **validated_data)
