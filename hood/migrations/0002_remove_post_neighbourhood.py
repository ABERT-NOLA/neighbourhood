# Generated by Django 3.1 on 2020-11-02 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='neighbourhood',
        ),
    ]
