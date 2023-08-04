from author.viewsets import ArticleViewsets,MagazineViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles',ArticleViewsets)
router.register('magazines',MagazineViewsets)
