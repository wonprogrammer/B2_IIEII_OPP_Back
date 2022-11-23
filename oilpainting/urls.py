from django.urls import path
from oilpainting import views


urlpatterns = [
    path('', views.ArticleView.as_view(), name='article_view'),
    path('imgtoop/', views.ImageUploadview.as_view(), name='image_upload_view'),
]