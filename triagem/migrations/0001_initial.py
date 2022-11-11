# Generated by Django 4.1.2 on 2022-11-09 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0002_alter_animal_data_de_nascimento_pet_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Triagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sintomas', models.CharField(max_length=2000)),
                ('nome_do_pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
            ],
        ),
    ]
