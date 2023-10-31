# Generated by Django 4.2.6 on 2023-10-31 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clauses', '0003_rename_date_added_clause_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clause_vote',
            old_name='clause_id',
            new_name='clause',
        ),
        migrations.RemoveField(
            model_name='clause_vote',
            name='downs',
        ),
        migrations.RemoveField(
            model_name='clause_vote',
            name='ups',
        ),
        migrations.AddField(
            model_name='clause_vote',
            name='user',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='clause_vote',
            name='value',
            field=models.CharField(choices=[('U', 'upvote'), ('D', 'downvote'), ('R', 'report')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='clause',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
