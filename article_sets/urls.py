from django.urls import path

from .views import ArticleView


app_name = "articles_sets"

urlpatterns = [
    path('articles/', ArticleView.as_view({'get': 'list'})),
    path('articles/<int:pk>', ArticleView.as_view({'get': 'retrive'})),
]
