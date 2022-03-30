# Generated by Django 3.2.12 on 2022-03-28 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_text', models.CharField(max_length=4096)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SummaryText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_text', models.CharField(max_length=4096)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('original_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nlp0.originaltext')),
            ],
        ),
    ]