# Generated by Django 3.2.13 on 2022-10-24 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoria')),
                ('idade', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Campeonato',
                'verbose_name_plural': 'Campeonatos',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(max_length=100, verbose_name='Sexo')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('tecnico', models.CharField(max_length=100, verbose_name='Técnico')),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('pontostimeA', models.IntegerField(null=True, verbose_name='Pontos time A')),
                ('pontostimeB', models.IntegerField(null=True, verbose_name='Pontos time B')),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.campeonato', verbose_name='Campeonato')),
                ('timeA', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='timeA', to='ecommerce.time', verbose_name='Time A')),
                ('timeB', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='timeB', to='ecommerce.time', verbose_name='Time B')),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('posicao', models.CharField(max_length=100, verbose_name='Posição')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ecommerce.categoria', verbose_name='Categoria')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.time', verbose_name='Time')),
            ],
            options={
                'verbose_name': 'Jogador',
                'verbose_name_plural': 'Jogadores',
            },
        ),
        migrations.CreateModel(
            name='Estatistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponto', models.IntegerField()),
                ('assistencia', models.IntegerField()),
                ('rebote', models.IntegerField()),
                ('turnover', models.IntegerField()),
                ('tempo', models.IntegerField()),
                ('faltas', models.IntegerField()),
                ('jogador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.jogador', verbose_name='Jogador')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.partida', verbose_name='Partida')),
            ],
        ),
        migrations.AddField(
            model_name='campeonato',
            name='times',
            field=models.ManyToManyField(to='ecommerce.Time', verbose_name='Times'),
        ),
    ]
