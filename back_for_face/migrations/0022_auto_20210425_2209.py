# Generated by Django 2.2.7 on 2021-04-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_for_face', '0021_remove_qr_door_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr',
            name='user_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
