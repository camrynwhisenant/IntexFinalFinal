# Generated by Django 3.2.9 on 2021-12-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpioidData', '0004_auto_20211206_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'state',
            },
        ),
    ]
