import unittest
from django.test import Permissao

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a permissao.
        self.permissao = Permissao()

    def test_details(self):
        # Issue a GET request.
        response = self.permissao.get('/permissao/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 permissoes.
        self.assertEqual(len(response.context['permissoes']), 11)