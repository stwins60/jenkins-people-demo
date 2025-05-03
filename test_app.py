import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_content(self):
        response = self.app.get('/')

        self.assertIn(b'Dangers of AI in Classrooms', response.data)
        self.assertIn(b'Data Privacy', response.data)
        self.assertIn(b'Over-reliance on AI', response.data)

if __name__ == '__main__':
    unittest.main()