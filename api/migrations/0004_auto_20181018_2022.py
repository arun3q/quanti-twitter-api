# Generated by Django 2.0.9 on 2018-10-18 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181018_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handler',
            name='id',
        ),
        migrations.AlterField(
            model_name='handler',
            name='twitterhandle',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]