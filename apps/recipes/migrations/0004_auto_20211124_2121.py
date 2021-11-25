# Generated by Django 3.2.3 on 2021-11-24 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='category',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.URLField(blank=True, default='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='name'),
        ),
    ]