from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from users.models import User


# Register your models here.
class UserAdmin(ModelAdmin):
    list_display = ['id', 'role', 'username', 'avatar_preview']
    list_display_links = ('id', 'role', 'username')

    def avatar_preview(self, obj):
        if obj:
            return mark_safe('<img src="{}" width="120" height="85" />'.format(obj.avatar.url))


admin.site.register(User, UserAdmin)
