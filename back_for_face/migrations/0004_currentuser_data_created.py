# Generated by Django 2.2.7 on 2021-04-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_for_face', '0003_auto_20210402_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentuser',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
