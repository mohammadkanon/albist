# Generated by Django 2.2.3 on 2019-07-04 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanPay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plan_pay', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_feature', models.CharField(max_length=100)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.Plan')),
                ('planpay', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.PlanPay')),
            ],
        ),
    ]
