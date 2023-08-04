from rest_framework import serializers
from . models import Article,Magazine,Author

# All Articles

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['article_title']

# All Magazine

class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = ['magazine_name']

# All article related to the author with <pk>

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'




