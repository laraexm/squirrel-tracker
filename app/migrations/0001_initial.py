# Generated by Django 3.0.5 on 2020-10-14 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(help_text='Unique ID of squirrel', max_length=100)),
            ],
        ),
    ]