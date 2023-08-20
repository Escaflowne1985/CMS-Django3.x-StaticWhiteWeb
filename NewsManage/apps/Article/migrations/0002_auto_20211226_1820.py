# Generated by Django 3.0.3 on 2021-12-26 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletag',
            name='add_user',
            field=models.ForeignKey(help_text='数据录入用户名称', on_delete=django.db.models.deletion.CASCADE, related_name='ATAddUser', to=settings.AUTH_USER_MODEL, verbose_name='数据录入用户'),
        ),
        migrations.AddField(
            model_name='articleitem',
            name='add_user',
            field=models.ForeignKey(help_text='数据录入用户名称', on_delete=django.db.models.deletion.CASCADE, related_name='AIAddUser', to=settings.AUTH_USER_MODEL, verbose_name='数据录入用户'),
        ),
        migrations.AddField(
            model_name='articleitem',
            name='category',
            field=models.ForeignKey(help_text='选择栏目所属类别，若没有请在文章类别管理中创建', on_delete=django.db.models.deletion.CASCADE, related_name='ArticleItemCategory', to='Article.ArticleCategory', verbose_name='栏目所属大类'),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='article_author',
            field=models.ForeignKey(help_text='数据录入用户名称', on_delete=django.db.models.deletion.CASCADE, related_name='AIAuthor', to=settings.AUTH_USER_MODEL, verbose_name='数据录入用户'),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='audit_user',
            field=models.ForeignKey(blank=True, help_text='审核用户名称', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AIAudit', to=settings.AUTH_USER_MODEL, verbose_name='审核用户'),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='category',
            field=models.ForeignKey(help_text='若没有需要类别请在文章类别管理中创建', on_delete=django.db.models.deletion.CASCADE, related_name='ArticleInfoCategory', to='Article.ArticleCategory', verbose_name='文章类别'),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='item',
            field=models.ForeignKey(help_text='选择文章所属栏目，若没有请在文章栏目管理中创建', on_delete=django.db.models.deletion.CASCADE, related_name='ArticleInfoItem', to='Article.ArticleItem', verbose_name='所属栏目'),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='若没有请在文章标签管理中创建', related_name='ArticleInfoTags', to='Article.ArticleTag', verbose_name='文章标签'),
        ),
        migrations.AddField(
            model_name='articlecategory',
            name='add_user',
            field=models.ForeignKey(help_text='数据录入用户名称', on_delete=django.db.models.deletion.CASCADE, related_name='ACAddUser', to=settings.AUTH_USER_MODEL, verbose_name='数据录入用户'),
        ),
    ]
