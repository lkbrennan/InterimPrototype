# Generated by Django 2.1.3 on 2018-12-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_type',
            field=models.CharField(choices=[('first', 'First Class'), ('second', 'Second Class'), ('third', 'Third Class'), ('fourth', 'Fourth Class'), ('fifth', 'Fifth Class'), ('sixth', 'Sixth Class')], default='first', max_length=8),
        ),
    ]
