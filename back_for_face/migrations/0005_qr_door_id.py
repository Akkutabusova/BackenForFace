# Generated by Django 2.2.7 on 2021-04-01 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_for_face', '0004_currentuser_data_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr',
            name='door_id',
            field=models.IntegerField(null=True),
        ),
    ]
