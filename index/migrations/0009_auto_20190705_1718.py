# Generated by Django 2.2.3 on 2019-07-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_delete_bestservices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topslider',
            name='slider_img',
            field=models.ImageField(default='default.jpg', null=True, upload_to='topslider'),
        ),
    ]
