
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        Post.objects.create(title="Test Post", content="Just a test", author=user)

    def test_string_representation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), post.title)
