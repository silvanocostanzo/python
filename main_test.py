from unittest import TestCase
from unittest.mock import patch, Mock



class TestMain(TestCase):
    @patch('main.Print.print_hi', return_value=9)
    def test_print(self, print_hi):
        res = print_hi()
        self.assertEqual(res, 9)

    @patch('main.Print')
    def test_posts(self, MockPost):
        post = MockPost()

        post.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  '
                        'of  the Galaxy\ lies a small unregarded yellow sun. '
            }
        ]

        response = post.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
