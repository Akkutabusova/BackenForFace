# Generated by Django 2.2.7 on 2021-04-01 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_for_face', '0010_auto_20210402_0453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentuser',
            old_name='my_user',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='currentuser',
            name='user_door',
        ),
        migrations.RemoveField(
            model_name='qr',
            name='current_user',
        ),
        migrations.RemoveField(
            model_name='qr',
            name='data_created',
        ),
        migrations.RemoveField(
            model_name='qr',
            name='door',
        ),
        migrations.AddField(
            model_name='currentuser',
            name='door_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='qr',
            name='door_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='qr',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Door',
        ),
    ]