# Generated by Django 3.1.3 on 2021-07-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainMap', '0017_auto_20210723_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='lock',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marina',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weir',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
