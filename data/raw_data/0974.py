# Generated by Django 4.1.4 on 2023-03-09 10:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_remove_movie_videos_delete_customuser_delete_movie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('age_limit', models.CharField(choices=[('All', 'All'), ('Kids', 'Kids')], max_length=5)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('file', models.FileField(upload_to='movies')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('type', models.CharField(choices=[('single', 'Single'), ('seasonal', 'Seasonal')], max_length=10)),
                ('flyer', models.ImageField(blank=True, null=True, upload_to='flyers')),
                ('age_limit', models.CharField(blank=True, choices=[('All', 'All'), ('Kids', 'Kids')], max_length=5, null=True)),
                ('videos', models.ManyToManyField(to='core.video')),
            ],
        ),
    ]