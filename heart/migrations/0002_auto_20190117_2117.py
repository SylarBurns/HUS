# Generated by Django 2.1.3 on 2019-01-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='belongToBoard',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='belongToComment',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reportStatus',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='comment',
            name='stance',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='comrelation',
            name='annoName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='comrelation',
            name='vote',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='postrelation',
            name='annoName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='postrelation',
            name='vote',
            field=models.IntegerField(blank=True),
        ),
    ]
