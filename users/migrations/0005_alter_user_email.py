# Generated by Django 4.1.7 on 2023-03-07 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_birth_date_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
