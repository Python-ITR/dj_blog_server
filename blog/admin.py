from django.contrib import admin
from .models import Tag, Category, Post

# Register your models here.


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    pass
