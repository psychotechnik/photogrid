from django.contrib import admin
from .models import Chessboard, Photo
from sorl.thumbnail.admin import AdminImageMixin


class PhotoInlineModelAdmin(AdminImageMixin, admin.TabularInline):
    model = Photo


class ChessBoardAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("name", "description")
    inlines = [PhotoInlineModelAdmin]

admin.site.register(Chessboard, ChessBoardAdmin)