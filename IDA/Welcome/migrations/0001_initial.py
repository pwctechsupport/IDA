# Generated by Django 4.2.7 on 2023-12-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomeUserFirstLogin',
            fields=[
                ('userloginid', models.AutoField(db_column='UserLoginID', primary_key=True, serialize=False)),
                ('username', models.TextField(db_column='Username')),
                ('password', models.TextField(db_column='Password')),
                ('lastlogin', models.DateTimeField(blank=True, db_column='LastLogin', null=True)),
            ],
            options={
                'db_table': 'WelcomeUserFirstLogin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WelcomeUserlogin',
            fields=[
                ('userloginid', models.AutoField(db_column='UserLoginID', primary_key=True, serialize=False)),
                ('username', models.TextField(db_column='Username')),
                ('password', models.TextField(db_column='Password')),
                ('lastlogin', models.DateTimeField(blank=True, db_column='LastLogin', null=True)),
            ],
            options={
                'db_table': 'WelcomeUserLogin',
                'managed': False,
            },
        ),
    ]
