# Generated by Django 4.1.3 on 2022-12-29 18:15

from django.db import migrations, models
import task_manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['deadline']},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelManagers(
            name='worker',
            managers=[
                ('objects', task_manager.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_completed',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Not started', 'Task not started'), ('In progress', 'Task in progress'), ('On review', 'Task on review'), ('Completed', 'Task completed')], default='Not started', max_length=70),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('No priority', 'No priority'), ('Low', 'Low priority'), ('Normal', 'Normal priority'), ('Urgent', 'Urgent priority')], default='No priority', max_length=70),
        ),
        migrations.AlterField(
            model_name='worker',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='username',
            field=models.CharField(max_length=69, null=True, unique=True),
        ),
    ]
