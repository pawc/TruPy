# Generated by Django 3.1 on 2020-08-25 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20200825_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='favrecord',
            name='recordId',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='favrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
