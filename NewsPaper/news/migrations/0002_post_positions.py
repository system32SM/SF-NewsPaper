# Generated by Django 4.2.6 on 2023-10-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='positions',
            field=models.CharField(choices=[('PA', 'Статья'), ('PN', 'Новость')], default='PA', max_length=2, verbose_name='Тип поста'),
        ),
    ]
