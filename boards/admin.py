from django.contrib import admin

from .models import Board, Topic, Post
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description', )


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'last_updated', 'board', 'starter')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'topic')


admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
