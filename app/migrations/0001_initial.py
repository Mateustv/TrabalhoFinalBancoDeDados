# Generated by Django 4.1.1 on 2023-02-09 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaComum',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id_area')),
                ('nome', models.CharField(max_length=120)),
                ('regras', models.TextField()),
                ('capacidade', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Gestao',
            fields=[
                ('id_gestao', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id_gestao')),
                ('nome', models.CharField(max_length=150)),
                ('dt_inicio', models.DateField(null=True, verbose_name='Data Início')),
                ('dt_fim', models.DateField(null=True, verbose_name='Data Fim')),
                ('atos', models.TextField()),
                ('estatuto', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='CPF')),
                ('nome', models.CharField(max_length=120)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=60)),
                ('dt_nasc', models.DateField(null=True, verbose_name='Data de Nascimento')),
                ('cargo', models.CharField(choices=[('Morador', 'Morador'), ('Síndico', 'Síndico'), ('Sub-Síndico', 'Sub-Síndico')], max_length=15, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id_unidade', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('bloco', models.CharField(max_length=10)),
                ('numero', models.CharField(max_length=10)),
                ('vaga', models.CharField(max_length=10)),
                ('placa', models.CharField(max_length=7)),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidade', to='app.proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='Reuniao',
            fields=[
                ('id_reuniao', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('data', models.DateField(null=True, verbose_name='Data da Reunião')),
                ('hora', models.TimeField(null=True, verbose_name='Horário da Reunião')),
                ('pauta', models.TextField()),
                ('local', models.CharField(max_length=60)),
                ('relatorio', models.FileField(upload_to='pdf/')),
                ('presenca', models.ManyToManyField(to='app.proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='PresencaReuniao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('obs', models.TextField(blank=True)),
                ('presenca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reuniao', to='app.reuniao')),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id_ocorrencia', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=150, null=True)),
                ('descricao', models.TextField()),
                ('nome', models.CharField(max_length=100, null=True)),
                ('data', models.DateField(null=True, verbose_name='Data da Ocorrência')),
                ('hora', models.TimeField(null=True, verbose_name='Horário da Ocorrência')),
                ('arquivo', models.FileField(upload_to='arq/')),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areacomum', to='app.areacomum')),
                ('id_gestao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gestao', to='app.gestao')),
                ('id_unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidade', to='app.unidade')),
            ],
        ),
        migrations.AddField(
            model_name='gestao',
            name='sindico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sindico', to='app.proprietario'),
        ),
        migrations.AddField(
            model_name='gestao',
            name='subsindico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsindico', to='app.proprietario'),
        ),
    ]
