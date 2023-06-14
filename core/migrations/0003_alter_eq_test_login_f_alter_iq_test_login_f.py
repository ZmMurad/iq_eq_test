# Generated by Django 4.2.2 on 2023-06-14 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_eq_test_login_f_alter_iq_test_login_f'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eq_test',
            name='login_f',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.unique_login'),
        ),
        migrations.AlterField(
            model_name='iq_test',
            name='login_f',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.unique_login'),
        ),
    ]