# Generated by Django 3.2.7 on 2021-10-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
