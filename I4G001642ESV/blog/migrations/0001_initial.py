# Generated by Django 4.0.5 on 2022-06-17 15:50

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('published_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
