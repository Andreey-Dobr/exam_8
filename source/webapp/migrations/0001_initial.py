# Generated by Django 2.2 on 2020-09-26 06:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('category', models.CharField(choices=[('services', 'услуги'), ('products', 'товары'), ('relaxation', 'отдых'), ('no_category', 'без категории')], default='no_category', max_length=100, verbose_name='категория')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=400, verbose_name='Комментарий')),
                ('appraisal', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='webapp.Product', verbose_name='Продукт')),
            ],
        ),
    ]
