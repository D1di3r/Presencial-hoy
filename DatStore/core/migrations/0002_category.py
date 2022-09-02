# Generated by Django 4.1 on 2022-09-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre de la categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'db_table': 'categoria',
                'ordering': ['id'],
            },
        ),
    ]
