# Generated by Django 3.2.5 on 2023-08-02 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
    ]
