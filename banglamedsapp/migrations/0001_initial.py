# Generated by Django 2.2.4 on 2019-10-15 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('Id', models.AutoField(db_column='DistrictID', primary_key=True, serialize=False)),
                ('DistrictCode', models.CharField(db_column='DistrictCode', max_length=50)),
                ('DistrictName', models.CharField(db_column='DistrictName', max_length=100)),
                ('DivisionId', models.IntegerField(db_column='DivisionID')),
            ],
            options={
                'db_table': 'district',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('Id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('UserName', models.CharField(db_column='UserName', max_length=255)),
                ('Mobile', models.CharField(db_column='Mobile', max_length=255)),
                ('Email', models.CharField(db_column='Email', max_length=255, unique=True)),
                ('IsUsed', models.CharField(db_column='IsUsed', default='N', max_length=10)),
                ('Status', models.CharField(db_column='Status', default='1', max_length=10)),
                ('Remark', models.CharField(db_column='Remark', default='1', max_length=255)),
                ('EntryDate', models.DateTimeField(auto_now_add=True, db_column='EntryDate')),
                ('DistrictId', models.ForeignKey(db_column='DistrictId', on_delete=django.db.models.deletion.CASCADE, to='banglamedsapp.District')),
            ],
            options={
                'db_table': 'RegisteredUser',
                'managed': True,
            },
        ),
    ]
