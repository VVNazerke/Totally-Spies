from django.db import models


class Author(models.Model):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
