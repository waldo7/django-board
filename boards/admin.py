from django.contrib import admin

from .models import Board
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description', )


admin.site.register(Board, BoardAdmin)
