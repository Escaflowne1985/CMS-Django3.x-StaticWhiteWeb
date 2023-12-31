# Generated by Django 3.0.3 on 2021-12-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20211230_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userserverlog',
            old_name='log_remark',
            new_name='remark',
        ),
        migrations.RenameField(
            model_name='userserverlog',
            old_name='log_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='userserverlog',
            old_name='log_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='userserverlog',
            old_name='log_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='userserverlog',
            old_name='log_user',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userserverlog',
            name='log_content',
        ),
        migrations.AddField(
            model_name='userserverlog',
            name='content',
            field=models.TextField(blank=True, default='', help_text='记录的操作日志内容', null=True, verbose_name='日志内容'),
        ),
    ]
