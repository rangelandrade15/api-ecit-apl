# Generated by Django 5.1.4 on 2024-12-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_disciplina'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='professores/', verbose_name='Foto'),
        ),
    ]
