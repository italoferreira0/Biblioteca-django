# Generated by Django 5.1.5 on 2025-01-25 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('senha', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Usuario',
            },
        ),
    ]
