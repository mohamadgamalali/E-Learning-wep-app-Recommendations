# Generated by Django 2.1.7 on 2019-04-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyId', models.CharField(max_length=250)),
                ('companyName', models.CharField(max_length=250)),
                ('companyInterest', models.CharField(max_length=250)),
            ],
        ),
    ]