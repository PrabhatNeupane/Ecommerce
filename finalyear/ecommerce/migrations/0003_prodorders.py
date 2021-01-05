# Generated by Django 2.2.10 on 2020-05-06 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='prodorders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('phone', models.CharField(default='', max_length=15)),
            ],
        ),
    ]