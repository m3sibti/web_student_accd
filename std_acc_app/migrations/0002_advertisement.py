# Generated by Django 3.1.3 on 2020-11-25 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('std_acc_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('weekly_rent', models.FloatField(default=0)),
                ('available_from', models.CharField(max_length=20)),
                ('bond_amount', models.FloatField()),
                ('img', models.ImageField(upload_to='static/pictures')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('add_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
