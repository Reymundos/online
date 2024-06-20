from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import (Course, CourseThema, Comment, News, Video, LikeDislike)
from .serializer import (CourseSerializer, CourseThemaSerializer, CommentSerializer, NewsSerializer, VideoSerializer, LikeDislikeSerializer)


class CourseAPIListCreateView(ListCreateAPIView):
    """Mavjud kurslarni barchasini ko'rish va yangi yaratish uchun"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseAPIGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """Mavjud kurslarni id bo'yicha ko'rish, yangilash va o'chirish uchun"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseThemaAPIListCreateView(ListCreateAPIView):
    queryset = CourseThema.objects.all()
    serializer_class = CourseThemaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class CourseThemaAPIGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CourseThema.objects.all()
    serializer_class = CourseThemaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentAPIListCreateView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentAPIGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NewsAPIListCreateView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NewsAPIGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class LikeDislikeAPIListCreateView(GenericAPIView):
    serializer_class = LikeDislikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def post(self, request, *args, **kwargs):
    #     course_thema_id = self.kwargs.get('course_thema_id')
    #     vote = request.data.get('vote')
    #     user = request.user
    #
    #     # course_thema obyektini olish yoki 404 qaytarish
    #     course_thema = get_object_or_404(CourseThema, id=course_thema_id)
    #
    #     # vote qiymatini tekshirish
    #     if vote not in [LikeDislike.LIKE, LikeDislike.DISLIKE]:
    #         return Response({"message": "Invalid vote value"}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     like_dislike, created = LikeDislike.objects.get_or_create(user=user, course_thema=course_thema)
    #
    #     if not created:
    #         if like_dislike.vote == vote:
    #             like_dislike.delete()
    #             return Response({"message": "Vote removed"}, status=status.HTTP_204_NO_CONTENT)
    #         else:
    #             like_dislike.vote = vote
    #             like_dislike.save()
    #             return Response({"message": "Vote updated"}, status=status.HTTP_200_OK)
    #     else:
    #         like_dislike.vote = vote
    #         like_dislike.save()
    #         return Response({"message": "Vote added"}, status=status.HTTP_201_CREATED)


class LikeDislikeAPIGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class VideoAPIListCreateView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class VideoAPIGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
