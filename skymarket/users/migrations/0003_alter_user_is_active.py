# Generated by Django 4.0.5 on 2022-06-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_is_active_alter_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]