
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ('cidade',)
    search_fields = ('nome',)
    list_display = ("nome", 'pk', 'cidade', 'id', 'image_tag')
    exclude = ('responsavel', 'created_date', 'image_tag')

    def save_model(self, request, obj, form, change):
        obj.responsavel = request.user
        obj.save()

# Register your models here.
admin.site.register(Post, PostAdmin)
