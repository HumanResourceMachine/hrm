# Generated by Django 2.0.5 on 2018-06-02 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.CharField(default='?', max_length=50),
        ),
    ]
