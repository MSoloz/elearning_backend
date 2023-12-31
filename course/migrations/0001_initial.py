# Generated by Django 4.2.3 on 2023-08-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image_path', models.ImageField(upload_to='images/')),
                ('video_path', models.FileField(upload_to='videos/')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
