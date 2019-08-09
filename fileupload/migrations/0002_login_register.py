# Generated by Django 2.2.4 on 2019-08-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
    ]