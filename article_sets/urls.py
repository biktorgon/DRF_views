from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet


app_name = "articles_sets"

router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='user')

urlpatterns = router.urls
