# Generated by Django 2.2.7 on 2021-04-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_for_face', '0022_auto_20210425_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='door',
            name='qr_string',
            field=models.CharField(max_length=200, null=True),
        ),
    ]