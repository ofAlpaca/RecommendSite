# Generated by Django 2.0 on 2018-01-01 07:40

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_UserArticle',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('ck_content', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='Content')),
                ('last_mod', models.DateTimeField()),
                ('tags', multiselectfield.db.fields.MultiSelectField(choices=[('a', 'Asia'), ('b', 'Blacks'), ('c', 'Celebrity'), ('d', 'Dank'), ('f', 'Female'), ('g', 'Games'), ('h', 'Hitler'), ('i', 'Internet'), ('j', 'JoJoRef'), ('k', 'Kim Jong-un'), ('l', 'Lifehack'), ('m', 'Math'), ('n', 'Net Neutrality'), ('p', 'PC'), ('r', 'Religion'), ('r2', 'Russian'), ('s', 'Singer'), ('t', 'Taiwan'), ('u', 'USA'), ('v', 'Vehicle'), ('w', 'Welcom to HELL'), ('y', 'Yes/No')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='UserLikePost',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='article.Post')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstname_field', models.CharField(max_length=50)),
                ('lastname_field', models.CharField(max_length=50)),
                ('intro', models.TextField(blank=True, max_length=255)),
                ('photo_url', models.URLField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('subers', models.ManyToManyField(blank=True, related_name='_userprofile_subers_+', to=settings.AUTH_USER_MODEL)),
                ('subs', models.ManyToManyField(blank=True, related_name='_userprofile_subs_+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userlikepost',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='m_userarticle',
            name='readed_article',
            field=models.ManyToManyField(blank=True, related_name='_m_userarticle_readed_article_+', to='article.Post'),
        ),
    ]
