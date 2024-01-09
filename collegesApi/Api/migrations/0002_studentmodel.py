# Generated by Django 4.2.7 on 2024-01-04 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=6)),
                ('dateOfBirth', models.DateField()),
                ('address', models.TextField()),
                ('contactNo', models.BigIntegerField()),
                ('emailId', models.EmailField(max_length=50, unique=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.collegemodel')),
            ],
        ),
    ]
