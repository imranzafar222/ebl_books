# Generated by Django 4.0.2 on 2022-02-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(),
        ),
    ]