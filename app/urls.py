from django.urls import path
from .views import (CourseAPIListCreateView, CourseAPIGetUpdateDeleteView, CourseThemaAPIListCreateView,
                    CourseThemaAPIGetUpdateDeleteView, LikeDislikeAPIListCreateView, LikeDislikeAPIGetUpdateDeleteView,
                    VideoAPIListCreateView, VideoAPIGetUpdateDeleteView,
                    NewsAPIListCreateView, NewsAPIGetUpdateDeleteView)

urlpatterns = [
    path('course/', CourseAPIListCreateView.as_view()),
    path('course/<int:pk>/', CourseAPIGetUpdateDeleteView.as_view()),
    path('course-thema/', CourseThemaAPIListCreateView.as_view()),
    path('course-thema/<int:pk>/', CourseThemaAPIGetUpdateDeleteView.as_view()),
    path('search/', CourseThemaAPIListCreateView.as_view()),
    path('like/', LikeDislikeAPIListCreateView.as_view()),
    path('like/<int:pk>/', LikeDislikeAPIGetUpdateDeleteView.as_view()),
    path('video/', VideoAPIListCreateView.as_view()),
    path('video/<int:pk>/', VideoAPIGetUpdateDeleteView.as_view()),
    path('news/', NewsAPIListCreateView.as_view()),
    path('news/<int:pk>', NewsAPIGetUpdateDeleteView.as_view()),
]
