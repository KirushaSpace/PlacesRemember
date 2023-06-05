from django.test import TestCase, RequestFactory
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth.models import User
from .formss import NoteForm
from .models import Note
from .views import home


class HomeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем пользователя для тестов
        user = User.objects.create_user(username='testuser', password='testpass')

        # Создаем несколько заметок для пользователя
        Note.objects.create(user=user, title='Note 1', text='First note', lat=0.0, lon=0.0)
        Note.objects.create(user=user, title='Note 2', text='Second note', lat=0.0, lon=0.0)
        Note.objects.create(user=user, title='Note 3', text='Third note', lat=0.0, lon=0.0)

    def setUp(self):
        # Создаем экземпляр RequestFactory для создания тестовых запросов
        self.factory = RequestFactory()

        # Создаем клиент для отправки запросов
        self.client = Client()


    def test_home_page(self):
        user = User.objects.get(username='testuser')
        self.client.force_login(user)

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTrue('notes' in response.context)


    def test_create_note_page(self):
        user = User.objects.get(username='testuser')
        self.client.force_login(user)

        response = self.client.get(reverse('create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maps.html')
        self.assertIs(response.context['form'], NoteForm)
        self.assertIsInstance(response.context['notes'], object)


    def test_home_view_with_authenticated_user(self):
        # Создаем аутентифицированного пользователя для тестов
        user = User.objects.get(username='testuser')
        self.client.force_login(user)

        response = self.client.get(reverse('home'))

        self.assertTemplateUsed(response, 'index.html')

        self.assertTrue('notes' in response.context)
        notes = response.context['notes']
        self.assertEqual(notes.count(), 3)  # Проверяем, что получены все 3 заметки пользователя

        for note in notes:
            self.assertTrue(hasattr(note, 'user'))
            self.assertTrue(hasattr(note, 'title'))
            self.assertTrue(hasattr(note, 'text'))
            self.assertTrue(hasattr(note, 'lat'))
            self.assertTrue(hasattr(note, 'lon'))
            self.assertTrue(hasattr(note, 'created'))


    def test_home_view_with_anonymous_user(self):
        # Создаем GET-запрос к home view от анонимного пользователя
        self.client.logout()
        response = self.client.get(reverse('home'))

        self.assertRedirects(response, '/login/?next=/home/')


    def test_login_page_with_authenticated_user(self):
        user = User.objects.get(username='testuser')
        self.client.force_login(user)

        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))


    def test_login_page_with_anonymous_user(self):
        self.client.logout()

        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)


    def test_logout(self):
        response = self.client.get(reverse('logout'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/logout/')
        self.assertFalse('_auth_user_id' in self.client.session)
