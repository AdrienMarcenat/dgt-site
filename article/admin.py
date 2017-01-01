from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 20}, )},
    }

admin.site.register(Article, ArticleAdmin)
admin.site.register(User)
