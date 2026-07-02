from django.test import TestCase
from apl.models import Categoria

# Create your tests here.
class PruebaBasica(TestCase):
    def test_verificar_entorno(self):
        """una prueba simple para validar que CI/CD funciona"""
        self.assertEqual(1+1+2)
        
    def test_crear_categoria(self):
        """prueba Basica de base de daros en memoria""" 
        # las consultas e inserciones van a DENTRO de las funciones
        Categoria.objects.create(nombre='Frijol')
        consulta = Categoria.objects.filter(nombre='Frijol')
        self.assertTrue(consulta.exists())
        

        
        
        