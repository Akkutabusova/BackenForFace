# Generated by Django 2.2.7 on 2021-04-01 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back_for_face', '0006_auto_20210402_0444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentuser',
            name='door_id',
        ),
        migrations.AddField(
            model_name='currentuser',
            name='door',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='back_for_face.QR'),
        ),
    ]