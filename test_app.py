import unittest
from flask import Flask
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_booking(self):
        data = {
            'movie_id': '1',
            'showtime': '12:00 PM',
            'num_tickets': '2'
        }
        response = self.app.post('/book', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Booking successful', response.data)

    def test_invalid_movie_id(self):
        data = {
            'movie_id': '10',
            'showtime': '12:00 PM',
            'num_tickets': '2'
        }
        response = self.app.post('/book', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Movie not found', response.data)

    def test_invalid_showtime(self):
        data = {
            'movie_id': '1',
            'showtime': '9:00 AM',
            'num_tickets': '2'
        }
        response = self.app.post('/book', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Showtime not available', response.data)

    def test_invalid_num_tickets(self):
        data = {
            'movie_id': '1',
            'showtime': '12:00 PM',
            'num_tickets': '0'
        }
        response = self.app.post('/book', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid number of tickets', response.data)

if __name__ == '__main__':
    unittest.main()
