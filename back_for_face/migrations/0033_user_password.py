# Generated by Django 2.2.7 on 2021-04-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_for_face', '0032_remove_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256, null=True),
        ),
    ]