from django.contrib import admin

from book import models


@admin.register(models.Author)
@admin.register(models.Genre)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount', 'author', 'genre', )
