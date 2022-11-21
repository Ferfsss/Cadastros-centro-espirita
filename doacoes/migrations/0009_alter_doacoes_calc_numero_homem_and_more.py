# Generated by Django 4.1.1 on 2022-11-03 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacoes', '0008_doacoes_calcados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacoes',
            name='calc_numero_homem',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doacoes',
            name='calc_numero_mulher',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doacoes',
            name='infant_mulher',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='doacoes',
            name='numero_homem',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doacoes',
            name='numero_mulher',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doacoes',
            name='telefone',
            field=models.IntegerField(),
        ),
    ]