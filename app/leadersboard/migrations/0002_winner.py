# Generated by Django 5.0.6 on 2024-06-21 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadersboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leadersboard.user')),
            ],
        ),
    ]