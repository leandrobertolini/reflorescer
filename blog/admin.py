
from django.contrib import admin
from .models import Componentes
from .models import Alas


class PostAdmin(admin.ModelAdmin):
    list_filter = ('ala','cidade','manequim')
    search_fields = ('nome',)
    list_display = ('nome', 'ala', 'cidade', 'foto', 'pagamento')
    exclude = ('responsavel', 'created_date')

    def save_model(self, request, obj, form, change):
        obj.responsavel = request.user
        obj.save()

class AlasAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    list_display = ('nome', 'componentes')

# Register your models here.
admin.site.register(Componentes, PostAdmin)
admin.site.register(Alas,AlasAdmin)