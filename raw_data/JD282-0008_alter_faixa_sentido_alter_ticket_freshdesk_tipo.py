# Generated by Django 4.1 on 2022-09-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnit_bi', '0007_alter_ticket_freshdesk_prioridade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faixa',
            name='sentido',
            field=models.CharField(choices=[('C', 'CRESCENTE'), ('D', 'DECRESCENTE')], max_length=11),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='tipo',
            field=models.CharField(choices=[('Equipamento Offline', 'Equipamento Offline'), ('Aferição', 'Aferição'), ('infraestrutura', 'infraestrutura'), ('Falha de Camera', 'Falha de Camera'), ('PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS', 'PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS'), ('Outro', 'Outro'), ('OCR', 'OCR'), ('Enquadramento', 'Enquadramento'), ('Implantação / ajuste de sinalização', 'Implantação / ajuste de sinalização'), ('Ajuste Fino', 'Ajuste Fino'), ('Falha de disco', 'Falha de disco'), ('Conectorização', 'Conectorização'), ('Ajuste de Display', 'Ajuste de Display'), ('Manutenção Preventiva', 'Manutenção Preventiva'), ('Falha de infração', 'Falha de infração'), ('Instalação / Reparo de cabo lógico', 'Instalação / Reparo de cabo lógico'), ('Implantação/Reparo de sinalização vertical', 'Implantação/Reparo de sinalização vertical'), ('Poda / Roçada', 'Poda / Roçada'), ('Instalação / Reparo de energia eletrica', 'Instalação / Reparo de energia eletrica'), ('Manutenção corretiva', 'Manutenção corretiva'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Iluminador', 'Iluminador'), ('Sem passagem / Não infracionando', 'Sem passagem / Não infracionando'), ('Ajuste de Imagem', 'Ajuste de Imagem'), ('Internet', 'Internet'), ('Implantação/Reparo de sinalização horizontal', 'Implantação/Reparo de sinalização horizontal'), ('Configuração de envio SIOR', 'Configuração de envio SIOR'), ('Solicitação de Análise', 'Solicitação de Análise')], max_length=100, null=True),
        ),
    ]