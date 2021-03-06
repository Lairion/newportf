# Generated by Django 2.0.7 on 2018-07-07 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOfSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Category name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Category of Skills',
                'verbose_name_plural': 'Categories of Skills',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Skill name')),
                ('image', models.ImageField(blank=True, upload_to='skill_logo/%Y/%m/%d/', verbose_name='Skill logo')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='skills.CategoryOfSkills', verbose_name='Category of skills')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
