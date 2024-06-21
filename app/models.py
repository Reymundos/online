from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


class Course(models.Model):
    """Kurslar uchun model"""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CourseThema(models.Model):
    """Kurslarning mavzulari uchun model"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


def file_size(value):
    """Video hajmini cheklash uchun funksiya"""
    limit = 1000 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 1000 MB.')


class Video(models.Model):
    """Videolar uchun model"""
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    course_thema = models.ForeignKey(CourseThema, on_delete=models.SET_NULL, null=True)
    video = models.FileField(upload_to='news/video/', help_text='Faqat! "MP4, MOV va AVI "', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'AVI']), file_size
    ])

    def __str__(self):
        return self.course_thema.name


class Comment(models.Model):
    """Darslarga izoh qoldirish uchun model"""
    course_thema = models.ForeignKey(CourseThema, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)


class LikeDislike(models.Model):
    """darsni baholash uchun model"""
    LIKE = 1
    MIDDLE = 0
    DISLIKE = -1

    VOTE_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (MIDDLE, 'Middle')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_thema = models.ForeignKey(CourseThema, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'course_thema')


class News(models.Model):
    """dasturdai yangilanishlar haqida habar beridh uchun model"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=News)
def send_update_email(sender, instance, created, **kwargs):
    if created:
        subject = f"New post: {instance.title}"
        message = f"Check out the new post: {instance.content}"
        users = User.objects.all()
        recipient_list = [user.email for user in users if user.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
