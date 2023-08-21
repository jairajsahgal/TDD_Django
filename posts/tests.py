from django.test import TestCase
from posts.models import Post
import string
from http import HTTPStatus
import secrets
# Create your tests here.

class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.all().count()

        self.assertEqual(posts,0)
    
    def test_string_rep_of_objects(self):

        post = Post.objects.create(
            title="Test Body",
            body="Test Body"
        )

        self.assertEqual(str(post),post.title)


class HomepageTest(TestCase):
    def setUp(self) -> None:
        for i in range(10):
            characters = string.ascii_letters + string.digits
            title = "Sample Test {i}".format(i=i)
            body = ''.join(secrets.choice(characters) for _ in range(200))
            Post.objects.create(title=title,body=body)
        
    def test_homepage_returns_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response,'posts/index.html')
        self.assertEqual(response.status_code,HTTPStatus.OK)
    
    def test_homepage_returns_post_list(self):
        response = self.client.get('/')
        
        self.assertContains(response,"Sample Test 5")
        self.assertContains(response,"Sample Test 4")
