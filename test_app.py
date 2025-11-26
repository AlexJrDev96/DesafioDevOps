import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em werkzeug 
if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 

    def test_get_items(self):
        # Testa se a rota /items retorna a lista corretamente
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        # Verifica se "item1" está dentro da lista retornada
        self.assertIn("item1", response.json['items'])

    def test_not_found(self):
        # Testa se uma rota inexistente retorna o erro 404 corretamente
        response = self.client.get('/rota-que-nao-existe')
        self.assertEqual(response.status_code, 404)

    def test_method_not_allowed(self):
        # Testa se usar POST em uma rota que só aceita GET retorna erro 405
        # A rota /items foi definida apenas com methods=['GET'] no app.py
        response = self.client.post('/items')
        self.assertEqual(response.status_code, 405)
    
   

if __name__ == '__main__':
    unittest.main()
