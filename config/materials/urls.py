from .apps import MaterialsConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, LessonDestroyAPIView, LessonUpdateAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
] + router.urls
