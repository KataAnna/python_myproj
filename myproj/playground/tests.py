from django.test import TestCase

from .models import Article, Publisher
from datetime import date

class ArticleTestCase(TestCase):

    def test_added_recently_true(self):
        article = Article(
            title='recently_added_article',
            pub_date=date.today(),
        )
        self.assertTrue(article.added_recently)
    
    def test_added_recently_false(self):
        article = Article(
            title='an_old_article',
            pub_date=date(2019, 1, 13),
        )
        self.assertFalse(article.added_recently)

class AnotherTestCase(TestCase):
    def test_always_fails(self):
        self.assertTrue(False)


class PlaygroundViewTestCase(TestCase):

    def setUp(self):
        publisher = Publisher.objects.create(
            first_name='John',
            last_name='Smith',
            email='john@smith.com',
        )
        for title in map(str, range(100)):
            Article.objects.create(
                title=title,
                pub_date=date.today(),
                publisher=publisher,
            )

    def test_index_content(self):
        response = self.client.get('/playground/')
        articles = [a for a in response.context['articles']]
        except_articles = [a for a in Article.objects.all()]
        self.assertEqual(articles, except_articles)
