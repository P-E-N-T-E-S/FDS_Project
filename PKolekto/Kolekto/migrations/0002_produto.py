# Generated by Django 4.1 on 2023-09-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Kolekto", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("foto1", models.ImageField(upload_to="fotos/")),
                ("foto2", models.ImageField(upload_to="fotos/")),
                ("foto3", models.ImageField(upload_to="fotos/")),
                ("foto4", models.ImageField(upload_to="fotos/")),
                ("nome_produto", models.CharField(max_length=100)),
                ("descricao", models.CharField(max_length=500)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=10)),
                ("qntd", models.PositiveSmallIntegerField()),
            ],
        ),
    ]
