# Generated by Django 3.2.9 on 2021-12-08 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizName', models.CharField(max_length=100)),
                ('quizScore', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('parentQuiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('isAns', models.BooleanField()),
                ('parentQuestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.question')),
            ],
        ),
    ]
