# Generated by Django 4.1.1 on 2022-10-05 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=50)),
                ('nip', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=50)),
                ('jabatan', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
