from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from fresh_app.models import Event, Category, Comment, Favourite


class EventAdmin(ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Event, EventAdmin)


class CategoryAdmin(ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class CommentAdmin(ModelAdmin):
    list_display = ['id', 'event', 'user', 'created_at']
    list_display_links = ('id', 'event')


admin.site.register(Comment, CommentAdmin)


class FavouriteAdmin(ModelAdmin):
    list_display = ['id', 'event', 'user']
    list_display_links = ('id', 'event')


admin.site.register(Favourite, FavouriteAdmin)
