# Generated by Django 3.1.4 on 2021-01-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20210122_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='feedback_funny',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='comments',
            field=models.ManyToManyField(null=True, to='post.BlogPostComment'),
        ),
    ]