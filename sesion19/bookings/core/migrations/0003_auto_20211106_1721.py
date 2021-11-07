# Generated by Django 3.2.9 on 2021-11-06 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20211106_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='nro_personas',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookigns', to=settings.AUTH_USER_MODEL),
        ),
    ]
