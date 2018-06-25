from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time', 'update_time')
    list_filter = ('create_time', 'update_time')


admin.site.register(models.Article, ArticleAdmin)
