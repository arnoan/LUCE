# Generated by Django 2.2 on 2019-06-30 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='purpose',
            field=models.TextField(null=True),
        ),
    ]
