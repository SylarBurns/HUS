# Generated by Django 2.1.3 on 2019-01-18 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0002_auto_20190117_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comrelation',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com_relation', to='heart.Comment'),
        ),
        migrations.AlterField(
            model_name='comrelation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com_relation', to='heart.User'),
        ),
        migrations.AlterField(
            model_name='postrelation',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_relation', to='heart.Post'),
        ),
        migrations.AlterField(
            model_name='postrelation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_relation', to='heart.User'),
        ),
    ]