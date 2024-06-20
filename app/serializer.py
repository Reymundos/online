from rest_framework.serializers import ModelSerializer

from .models import Course, CourseThema, LikeDislike, Comment, News, Video


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseThemaSerializer(ModelSerializer):
    class Meta:
        model = CourseThema
        fields = '__all__'


class LikeDislikeSerializer(ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
