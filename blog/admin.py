from django.contrib import admin
from django.db import connection
from .models.componente import Componente
from .models.ala import Ala
from .models.diretoria import Diretoria
from .models.ensaio import Ensaio

class DiretoriaAdmin(admin.ModelAdmin):
    list_filter = ('ala',)
    list_display = ('diretor','ala')


class AlasAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    list_display = ('nome', 'total_componentes','logo_ala') 


class ComponenteAdmin(admin.ModelAdmin):
    list_filter = ('ala','cidade','manequim')
    search_fields = ('nome',)
    list_display = ('nome', 'ala', 'cidade', 'foto_comp', 'pagamento', 'carteirinha', 'obs')
    exclude = ('responsavel', 'created_date')

    def save_model(self, request, obj, form, change):
        obj.responsavel = request.user
        obj.save()

    def get_queryset(self, request):
        diretoria = Diretoria.objects.filter(diretor=request.user)
        return Componente.objects.filter(ala_id__in = [x.ala_id for x in diretoria.all()]).all()


class EnsaioAdmin(admin.ModelAdmin):
    list_filter = ('presenca',)
    list_display = ('componente','presenca','data_ensaio')



# Register your models here.
admin.site.register(Componente, ComponenteAdmin)
admin.site.register(Ala,AlasAdmin)
admin.site.register(Diretoria,DiretoriaAdmin)
admin.site.register(Ensaio,EnsaioAdmin)