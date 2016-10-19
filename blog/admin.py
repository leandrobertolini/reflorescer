# coding: utf-8
from django.contrib import admin
from .models.componente import Componente
from .models.ala import Ala
from .models.diretoria import Diretoria
from .models.ensaio import Ensaio
from django.contrib.admin import widgets
from django.forms.widgets import CheckboxSelectMultiple, SelectMultiple


class DiretoriaAdmin(admin.ModelAdmin):
    list_filter = ('ala',)
    list_display = ('diretor', 'ala')


class AlasAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    list_display = ('nome', 'total_componentes', 'logo_ala')
    exclude = ('responsavel',)

    def save_model(self, request, obj, form, change):
        obj.responsavel = request.user
        obj.save()

    def get_queryset(self, request):
        return Ala.objects.filter(responsavel=request.user)


class ComponenteAdmin(admin.ModelAdmin):
    list_filter = ('ala', 'cidade', 'manequim')
    search_fields = ('nome',)
    list_display = ('nome', 'nascimento', 'ala', 'cidade', 'foto_comp', 'pagamento', 'carteirinha', 'status', 'obs')
    exclude = ('responsavel', 'created_date')

    def save_model(self, request, obj, form, change):
        obj.responsavel = request.user
        obj.save()

    def get_queryset(self, request):
        diretoria = Diretoria.objects.filter(diretor=request.user)
        return Componente.objects.filter(ala_id__in=[x.ala_id for x in diretoria.all()]).all()


class EnsaioAdmin(admin.ModelAdmin):
    list_filter = ('presenca', 'data_ensaio', 'componente')
    list_display = ('get_componentes', 'presenca', 'ala', 'data_ensaio')
    filter_horizontal = ('componente',)

    def get_componentes(self, obj):
        return "\n".join([c.nome for c in obj.componente.all()])

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """
        Get a form Field for a ManyToManyField.
        """
        form_field = super(EnsaioAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
        form_field = db_field.formfield(**kwargs)
        form_field.queryset = Componente.objects.filter(responsavel=request.user)
        return form_field

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Get a form Field for a ForeignKey.
        """
        super(EnsaioAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        _func = db_field.formfield(**kwargs)
        _func.queryset = Ala.objects.filter(responsavel=request.user)
        return _func


# Register your models here.
admin.site.register(Componente, ComponenteAdmin)
admin.site.register(Ala, AlasAdmin)
admin.site.register(Diretoria, DiretoriaAdmin)
admin.site.register(Ensaio, EnsaioAdmin)
