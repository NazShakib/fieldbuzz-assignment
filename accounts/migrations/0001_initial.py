# Generated by Django 3.1.4 on 2020-12-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_tysinc_id', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=256)),
                ('pdf_tysnic_id', models.CharField(max_length=55)),
                ('created_at', models.CharField(max_length=256)),
            ],
        ),
    ]
