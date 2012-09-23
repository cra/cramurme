from content.models import Film, Article, MediaEntry, ID
from django.contrib import admin

def publish(modeladmin, request, queryset):
    queryset.update(is_published=True)
publish.short_description = "Publish selected articles"

def unpublish(modeladmin, request, queryset):
    queryset.update(is_published=False)
unpublish.short_description = "Mark selected articles as draft"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'tags', 'date_published', 'is_published')
    actions = [publish, unpublish]

class FilmAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'tags')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(ID)
admin.site.register(MediaEntry)
