# Generated by Django 2.2 on 2019-06-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabeleireiro',
            name='apelido',
            field=models.CharField(default=1, max_length=100, verbose_name='apelido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='validade_produto',
            field=models.DateField(verbose_name='validade produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valor_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='valor unitario'),
        ),
    ]