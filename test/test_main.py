import unittest
from main import app


class TestMain(unittest.TestCase):
    def test_should_return_200_for_access_index(self):
        self.test_main = app.test_client()
        response = self.test_main.get('/index.html')

        self.assertEqual("200 OK", response.status)

    def test_should_return_404_for_access_unknow_route(self):
        self.test_main = app.test_client()
        response = self.test_main.get('/random_route')

        self.assertEqual("404 NOT FOUND", response.status)

    def test_should_return_dir_index_when_access_route_with_only_slash(self):
        self.test_main = app.test_client()
        response = self.test_main.get('/')

        self.assertEqual("200 OK", response.status)


