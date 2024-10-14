# Generated by Django 5.1.2 on 2024-10-12 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO blog_article (
                id, title, content, category_id
            )
            SELECT id, title, content, category_id
            FROM article;

            INSERT INTO blog_article_authors (
                id, article_id, author_id
            )
            SELECT id, article_id, author_id
            FROM article_authors;
        """, reverse_sql="""
            INSERT INTO article (
                id, title, content, category_id
            )
            SELECT id, title, content, category_id
            FROM blog_article;

            INSERT INTO article_authors (
                id, article_id, author_id
            )
            SELECT id, article_id, author_id
            FROM blog_article_authors;
        """
        )
    ]
