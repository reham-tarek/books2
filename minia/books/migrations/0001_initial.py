# Generated by Django 3.1.3 on 2020-11-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('publishdate', models.DateField()),
                ('add_to_site_at', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=100)),
                ('Appropriate', models.CharField(choices=[('m', 'under 8'), ('f', '8-15'), ('a', 'adult')], max_length=2)),
            ],
        ),
    ]
