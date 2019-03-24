# Generated by Django 2.1 on 2019-03-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='family_name',
            new_name='house_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='member_address',
        ),
        migrations.AddField(
            model_name='family',
            name='house_address',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='family',
            name='house_memebrship',
            field=models.IntegerField(null=True),
        ),
    ]