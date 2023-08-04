from django.db import models

# Magazine

class Magazine(models.Model):
    magazine_name = models.CharField(max_length=100)
    magazine_issue = models.IntegerField()

    def __str__(self):
        return self.magazine_name

# Article

class Article(models.Model):
    article_title = models.CharField(max_length=255)
    article_content = models.TextField()
    publication_date = models.DateField()
    magazines = models.ManyToManyField(Magazine)

    def __str__(self):
        return self.article_title

# Author

class Author(models.Model):
    author = models.CharField(max_length=25)
    articles = models.ManyToManyField(Article)
    magazines = models.ManyToManyField(Magazine)

    def __str__(self):
        return self.author