# Generated by Django 3.0 on 2020-02-20 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_venda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
