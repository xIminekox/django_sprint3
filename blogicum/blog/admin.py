from django.contrib import admin
from .models import Post, Category, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "pub_date", "is_published")
    search_fields = ("title", "text")
    list_filter = ("is_published", "pub_date")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published")
    search_fields = ("name",)


admin.site.site_title = "Блог"
admin.site.site_header = "Администрирование блога"
