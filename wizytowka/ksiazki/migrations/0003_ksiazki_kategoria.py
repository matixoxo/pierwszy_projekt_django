# Generated by Django 3.1.2 on 2020-10-13 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ksiazki', '0002_auto_20201013_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='ksiazki',
            name='kategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ksiazki.kategoria'),
        ),
    ]
