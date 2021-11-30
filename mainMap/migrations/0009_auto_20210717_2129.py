# Generated by Django 3.1.3 on 2021-07-17 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainMap', '0008_auto_20210717_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lock',
            name='chunk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lock', to='mainMap.chunk'),
        ),
        migrations.CreateModel(
            name='Marina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('localization', models.CharField(max_length=30)),
                ('description', models.TextField(default='')),
                ('x_pos', models.IntegerField(default=0)),
                ('y_pos', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('chunk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marina', to='mainMap.chunk')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
