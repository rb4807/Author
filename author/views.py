from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article,Author
from .serializers import ArticleSerializer,AuthorSerializer

# All article related to the author with <pk>

@api_view(['GET'])
def author(request, id):
    try:
        data = Author.objects.get(id=id)
        serializer = AuthorSerializer(data)
        return Response(serializer.data)
    except Author.DoesNotExist:
        return Response({"Article": "Article not found"}, status=404)

# All article related to the magazine with <pk>

@api_view(['GET'])
def magazine(request, id):
    try:
        data = Article.objects.get(id=id)
        serializer = ArticleSerializer(data)
        return Response(serializer.data)
    except Article.DoesNotExist:
        return Response({"Article": "Article not found"}, status=404)
