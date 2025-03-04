from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, ResultViewSet, UserViewSet, UserDetailView

router = DefaultRouter()
router.register(r'results', ResultViewSet)
router.register(r'users', UserViewSet)  # Добавляем маршрут для пользователей

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserDetailView.as_view(), name='user-detail'),  # Новый маршрут
    path('', include(router.urls)),
]