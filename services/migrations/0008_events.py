# Generated by Django 2.1.5 on 2020-06-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20200623_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('event_title', models.CharField(max_length=400)),
                ('event_overview', models.TextField()),
                ('event_link', models.CharField(max_length=500)),
            ],
        ),
    ]
