from django.contrib import admin
from .models import Professor, Turma, Horario, Evento, Palestra, Disciplina

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'formacao_academica')
    search_fields = ('nome', 'email')
    list_filter = ('formacao_academica',)
    list_per_page = 20
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'telefone')
        }),
        ('Informações Profissionais', {
            'fields': ('formacao_academica', 'foto')
        }),
    )

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_per_page = 20

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('turma', 'dia_semana', 'hora_inicio', 'hora_fim')
    list_filter = ('dia_semana', 'turma')
    search_fields = ('turma__nome',)
    list_per_page = 20
    
    fieldsets = (
        ('Turma', {
            'fields': ('turma',)
        }),
        ('Horário', {
            'fields': ('dia_semana', 'hora_inicio', 'hora_fim')
        }),
    )

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'data', 'hora_inicio', 'hora_fim', 'local', 'professor_responsavel')
    list_filter = ('tipo', 'data', 'professor_responsavel')
    search_fields = ('titulo', 'descricao', 'local', 'professor_responsavel__nome')
    filter_horizontal = ('turmas',)
    date_hierarchy = 'data'
    list_per_page = 20
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'tipo')
        }),
        ('Data e Horário', {
            'fields': ('data', 'hora_inicio', 'hora_fim')
        }),
        ('Local e Responsáveis', {
            'fields': ('local', 'professor_responsavel', 'turmas')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('professor_responsavel')

@admin.register(Palestra)
class PalestraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'palestrante', 'categoria', 'data', 'hora_inicio', 'hora_fim', 'local', 'capacidade')
    list_filter = ('categoria', 'data', 'professor_responsavel')
    search_fields = ('titulo', 'palestrante', 'descricao', 'local')
    filter_horizontal = ('turmas_convidadas',)
    date_hierarchy = 'data'
    list_per_page = 20
    
    fieldsets = (
        ('Informações da Palestra', {
            'fields': ('titulo', 'categoria', 'descricao')
        }),
        ('Informações do Palestrante', {
            'fields': ('palestrante', 'email_palestrante', 'telefone_palestrante')
        }),
        ('Data e Local', {
            'fields': ('data', 'hora_inicio', 'hora_fim', 'local', 'capacidade')
        }),
        ('Público e Requisitos', {
            'fields': ('publico_alvo', 'requisitos')
        }),
        ('Turmas e Responsável', {
            'fields': ('professor_responsavel', 'turmas_convidadas')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('professor_responsavel')

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor', 'turma', 'dia_semana', 'hora_inicio', 'hora_fim')
    search_fields = ('nome', 'professor__nome', 'turma__nome')
    list_filter = ('dia_semana', 'professor', 'turma')
    list_per_page = 20
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'professor', 'turma')
        }),
        ('Horário', {
            'fields': ('dia_semana', 'hora_inicio', 'hora_fim')
        }),
    )