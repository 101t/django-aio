from django.contrib import admin

from ..models import Tokenizer


@admin.register(Tokenizer)
class TokenizerAdmin(admin.ModelAdmin):
    list_display = ("guid", "uidb64", "token",)
    search_fields = ("guid",)
