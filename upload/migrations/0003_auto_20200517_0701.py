# Generated by Django 3.0.3 on 2020-05-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20200517_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Uploads',
        ),
    ]