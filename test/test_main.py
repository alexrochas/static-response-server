import unittest

from server.__init__ import app


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

    def test_should_return_dir_index_when_access_deeper_route_ending_with_slash(self):
        self.test_main = app.test_client()
        response = self.test_main.get('/person/')

        self.assertEqual("200 OK", response.status)

    def test_should_return_dir_index_when_access_deeper_route_ending_without_format(self):
        self.test_main = app.test_client()
        response = self.test_main.get('/person')

        self.assertEqual("200 OK", response.status)

    def test_should_return_file_when_access_wildcard_route(self):
        self.test_main = app.test_client()
        response = self.test_main.get('/person/wildcard/')

        self.assertEqual("200 OK", response.status)

    def test_should_return_file_when_access_two_levels_wildcard_route(self):
        self.test_main = app.test_client()
        response = self.test_main.get('/person/wildcard/wildcard')

        self.assertEqual("200 OK", response.status)



