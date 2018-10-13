# Generated by Django 2.1.1 on 2018-10-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20181011_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
