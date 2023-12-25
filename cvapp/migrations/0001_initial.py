# Generated by Django 5.0 on 2023-12-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('experience', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('cv_attachment', models.FileField(blank=True, null=True, upload_to='cv_attachments/')),
            ],
        ),
    ]
