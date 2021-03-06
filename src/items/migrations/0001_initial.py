# Generated by Django 3.0.2 on 2020-04-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('itemId', models.AutoField(primary_key=True, serialize=False)),
                ('itemTitle', models.CharField(max_length=60)),
                ('status', models.CharField(choices=[('1', 'New'), ('2', 'Used')], default='1', max_length=20)),
                ('itemDescription', models.CharField(max_length=60)),
                ('itemOwner', models.CharField(max_length=60)),
            ],
        ),
    ]
