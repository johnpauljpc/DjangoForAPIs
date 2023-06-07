from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

# Create your tests here.
class TestPostModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='admino', email='admino@gmail.com', password='mypassword123')
        user.save()
        # user.save()
        print('----------  ', user)
        post = Post.objects.create(author = user, title = "second post", body="this is just a test..")
        print('-----------------------------')
        post.save()
        print(post)

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'admino')
        self.assertEqual(title, 'second post')
        self.assertEqual(body, 'this is just a test..')