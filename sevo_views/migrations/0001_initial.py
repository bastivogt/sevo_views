# Generated by Django 5.0.6 on 2024-05-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['birthday'],
            },
        ),
    ]