# Generated by Django 4.0.4 on 2022-05-08 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='dateDone',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='dateStart',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='project',
            name='meters',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='patternlnk',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='yarn',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
