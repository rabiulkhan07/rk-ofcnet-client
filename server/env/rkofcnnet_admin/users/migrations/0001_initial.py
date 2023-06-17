# Generated by Django 3.2.16 on 2023-03-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('empId', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('isActive', models.BooleanField()),
                ('isOnline', models.IntegerField()),
            ],
        ),
    ]
