# Generated by Django 5.0.6 on 2024-07-29 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_usuario_chave_pix_alter_usuario_cpf_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
    ]
