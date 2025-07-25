# Generated by Django 4.2.1 on 2025-07-05 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bsc_gen', '0003_bscentry_batch_id_bscentry_upload_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningGrowthBSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(max_length=255)),
                ('measure', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=255)),
                ('actual', models.CharField(max_length=255)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('batch_id', models.CharField(blank=True, max_length=10, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('skill_area', models.CharField(blank=True, help_text='Skill or knowledge area', max_length=255)),
                ('training_metric', models.CharField(blank=True, help_text='Training or development metric', max_length=255)),
                ('innovation_indicator', models.CharField(blank=True, help_text='Innovation indicator', max_length=255)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bsc_gen.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InternalBSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(max_length=255)),
                ('measure', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=255)),
                ('actual', models.CharField(max_length=255)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('batch_id', models.CharField(blank=True, max_length=10, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('process_name', models.CharField(blank=True, help_text='Internal process name', max_length=255)),
                ('efficiency_metric', models.CharField(blank=True, help_text='Process efficiency metric', max_length=255)),
                ('quality_indicator', models.CharField(blank=True, help_text='Quality indicator', max_length=255)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bsc_gen.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FinancialBSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(max_length=255)),
                ('measure', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=255)),
                ('actual', models.CharField(max_length=255)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('batch_id', models.CharField(blank=True, max_length=10, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('financial_metric', models.CharField(help_text='Specific financial metric (e.g., Revenue, Profit, ROI)', max_length=255)),
                ('currency', models.CharField(default='USD', help_text='Currency for financial metrics', max_length=10)),
                ('period', models.CharField(blank=True, help_text='Reporting period (Monthly, Quarterly, Annual)', max_length=50)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bsc_gen.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerBSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(max_length=255)),
                ('measure', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=255)),
                ('actual', models.CharField(max_length=255)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('batch_id', models.CharField(blank=True, max_length=10, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer_segment', models.CharField(blank=True, help_text='Target customer segment', max_length=255)),
                ('satisfaction_metric', models.CharField(blank=True, help_text='Customer satisfaction metric', max_length=255)),
                ('loyalty_indicator', models.CharField(blank=True, help_text='Customer loyalty indicator', max_length=255)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bsc_gen.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
