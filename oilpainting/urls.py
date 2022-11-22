from django.urls import path
from oilpainting import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.ArticleView.as_view(), name='article_view'),
]
