# Generated by Django 3.0 on 2021-04-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_for_face', '0033_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='phone',
        ),
        migrations.AddField(
            model_name='manager',
            name='username',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
