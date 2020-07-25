# Generated by Django 3.0.8 on 2020-07-24 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='src.User'),
        ),
        migrations.AddField(
            model_name='folder',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='src.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='home',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='src.Folder'),
        ),
    ]