# Generated by Django 5.1.4 on 2024-12-22 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora_fim',
            field=models.TimeField(verbose_name='Hora de Término'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora_inicio',
            field=models.TimeField(verbose_name='Hora de Início'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='local',
            field=models.CharField(max_length=200, verbose_name='Local'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='professor_responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='core.professor', verbose_name='Professor Responsável'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(choices=[('AULA_EXTRA', 'Aula Extra'), ('REUNIAO', 'Reunião'), ('WORKSHOP', 'Workshop'), ('PALESTRA', 'Palestra'), ('OUTRO', 'Outro')], max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='turmas',
            field=models.ManyToManyField(blank=True, related_name='eventos', to='core.turma', verbose_name='Turmas'),
        ),
    ]
