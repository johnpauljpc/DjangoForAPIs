from django.test import TestCase
from .models import Todo

# Create your tests here.
class TestTodoModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='code today', body = 'just testing the model, so chill', completed = False)

    def test_title(self):
        todo = Todo.objects.get(id=1)
        expects = 'code today'
        self.assertEqual(todo.title, expects)
        print('No Error1')

    def test_body(self):
        todo = Todo.objects.get(id=1)
        expects = 'just testing the model, so chill'
        self.assertEqual(todo.body, expects)
        print('No Error2')
