from rest_framework import viewsets
from . import models
from . import serializers

#Article
 
class ArticleViewsets(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

# Magazine

class MagazineViewsets(viewsets.ModelViewSet):
    queryset = models.Magazine.objects.all()
    serializer_class = serializers.MagazineSerializer

# Author

class AuthorViewsets(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer