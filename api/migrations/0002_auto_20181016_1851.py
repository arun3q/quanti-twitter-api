# Generated by Django 2.0.9 on 2018-10-16 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handler',
            name='toptweets',
        ),
        migrations.AddField(
            model_name='handler',
            name='tweets',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Tweets'),
        ),
        migrations.AddField(
            model_name='tweets',
            name='retweets',
            field=models.IntegerField(default=0),
        ),
    ]
