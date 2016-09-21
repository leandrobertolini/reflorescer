
from django.contrib import admin
from .models.componente import Componente
from .models.ala import Ala


class PostAdmin(admin.ModelAdmin):
    list_filter = ('ala','cidade','manequim')
    search_fields = ('nome',)
    list_display = ('nome', 'ala', 'cidade', 'foto_comp', 'pagamento', 'carteirinha', 'obs')
    exclude = ('responsavel', 'created_date')

    def save_model(self, request, obj, form, change):
        obj.responsavel = request.user
        obj.save()

class AlasAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    list_display = ('nome', 'total_componentes','logo_ala')

# Register your models here.
admin.site.register(Componente, PostAdmin)
admin.site.register(Ala,AlasAdmin)