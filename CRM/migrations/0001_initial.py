# Generated by Django 4.2.10 on 2024-02-17 20:26

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='level_of_life',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neme', models.CharField(max_length=15, verbose_name='درجه مالی')),
            ],
            options={
                'verbose_name': 'توان مالی',
                'verbose_name_plural': 'توان مالی',
            },
        ),
        migrations.CreateModel(
            name='marital_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'وضعیت تاهل',
                'verbose_name_plural': 'وضعیت تاهل',
            },
        ),
        migrations.CreateModel(
            name='membership_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='نوع عضویت')),
            ],
            options={
                'verbose_name': 'نوع عضویت',
                'verbose_name_plural': 'نوع عضویت',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45, verbose_name='نام')),
                ('last_name', models.CharField(max_length=45, verbose_name='خانوادگی')),
                ('user_name', models.CharField(blank=True, max_length=45, null=True, verbose_name='کد عضویت')),
                ('national_code', models.CharField(blank=True, max_length=45, null=True, verbose_name='کدملی')),
                ('image', models.ImageField(blank=True, upload_to='picture/', verbose_name='عکس')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='سن')),
                ('join_at', django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='تاریخ عضویت')),
                ('job', models.CharField(blank=True, max_length=45, null=True, verbose_name='شغل')),
                ('level_of_life', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRM.level_of_life', verbose_name='توان مالی')),
                ('marital_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRM.marital_status', verbose_name='وضعیت تاهل')),
                ('membership_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CRM.membership_type', verbose_name='نوع عضویت')),
                ('representative', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM.users', verbose_name='معرف')),
            ],
            options={
                'verbose_name': 'جدول اعضا',
                'verbose_name_plural': 'جدول اعضا',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='امتیاز')),
                ('date', models.DateField(blank=True, null=True, verbose_name='تاریخ')),
                ('monasebat', models.CharField(blank=True, max_length=45, null=True, verbose_name='مناسبت')),
                ('users_idusers', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CRM.users')),
            ],
            options={
                'verbose_name': 'امتیاز',
                'verbose_name_plural': 'امتیاز ها',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=45, verbose_name='تلفن')),
                ('identity', models.CharField(blank=True, max_length=45, null=True, verbose_name='مالکیت')),
                ('pkuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CRM.users', verbose_name='عضو')),
            ],
            options={
                'verbose_name': 'تلفن',
                'verbose_name_plural': 'تلفن ها',
            },
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=15, null=True, verbose_name='شهر')),
                ('number_of_region', models.IntegerField(blank=True, null=True, verbose_name='منطقه')),
                ('street', models.CharField(blank=True, max_length=15, null=True, verbose_name='خیابان')),
                ('detail_adress', models.CharField(blank=True, max_length=45, null=True, verbose_name='ادرس کامل')),
                ('idusers', models.ForeignKey(db_column='idusers', on_delete=django.db.models.deletion.DO_NOTHING, to='CRM.users', verbose_name='عضو')),
            ],
            options={
                'verbose_name': 'ادرس',
                'verbose_name_plural': 'ادرس ها ',
            },
        ),
    ]
