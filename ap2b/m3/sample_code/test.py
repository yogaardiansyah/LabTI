import unittest
from app import app

class FlaskLoginTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SECRET_KEY'] = 'testsecret'
        self.client = app.test_client()
        self.ctx = app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_home_redirects_to_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.location)

    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_login_success(self):
        response = self.client.post('/login', data={
            'username': 'admin',
            'password': 'password123'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)

    def test_login_failure(self):
        response = self.client.post('/login', data={
            'username': 'admin',
            'password': 'wrongpassword'
        }, follow_redirects=True)

        self.assertIn(b'Login Gagal', response.data)

    def test_dashboard_requires_login(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.location)

    def test_logout(self):
        self.client.post('/login', data={
            'username': 'admin',
            'password': 'password123'
        }, follow_redirects=True)
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Login', response.data)

if __name__ == '__main__':
    unittest.main()
