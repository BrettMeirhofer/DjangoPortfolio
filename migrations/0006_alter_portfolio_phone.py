# Generated by Django 4.0.4 on 2022-05-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_portfolio_portfoliolink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
