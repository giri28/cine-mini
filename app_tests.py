import unittest

from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_success_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_error_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)        


if __name__ == '__main__':
    unittest.main()
