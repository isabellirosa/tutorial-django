# Generated by Django 5.2.1 on 2025-05-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_rename_autor_livro_autores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editora',
            name='cidade',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='editora',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
