# Generated by Django 3.2.25 on 2024-11-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eggoz2',
            fields=[
                ('studentid', models.AutoField(primary_key=True, serialize=False)),
                ('studentname', models.CharField(max_length=100)),
                ('studentloc', models.TextField()),
                ('studentphon', models.IntegerField()),
                ('studentgen', models.CharField(choices=[('boy', 'boy'), ('girl', 'girl')], default=None, max_length=5)),
                ('addeddate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]