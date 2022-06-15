from django.test import TestCase, Client
from django.urls import resolve
from blog.views import home_page
from blog.models import Item

# Create your tests here.
class HomePageTest(TestCase):
    def test_url_resolve(self):
        found = resolve('/')
        self.assertTrue(found.func == home_page)

    def test_home_page(self):
        c = Client()
        response = c.get('/')
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Lista do zrobienia</title>', html)
        self.assertTrue(html.endswith('</html>\n'))
        self.assertTemplateUsed(response, 'home.html')

    def test_post(self):
        c = Client()
        response = self.client.post('/', data={'id_new_item': 'A new list item'})
        html = response.content.decode('utf8')

        self.assertIn('A new list item', html)

    def test_display_items(self):
        first_item = Item()
        first_item.text = 'First item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Second item'
        second_item.save()

        c = Client()
        response = self.client.get('/')
        html = response.content.decode('utf8')

        self.assertIn('First item', html)
        self.assertIn('Second item', html)

class ItemModelTest(TestCase):
    def test_save_retrieve_items(self):
        first_item = Item()
        first_item.text = 'First item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'First item')
        self.assertEqual(second_saved_item.text, 'Second item')