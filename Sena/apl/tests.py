#from django.test import TestCase
from apl.models import *
from config.wsgi import *
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

# listar
#consulta = Categoria.objects.all()
#print(consulta)

# insertar

#c = Categoria(nombre = 'frijol').save()
#consulta = Categoria.objects.all()
#print(consulta)

#Editar
#c = Categoria.objects.get(id=1)
#c.nombre = 'cocacola'
#c.save()
#print(c.nombre)

# Eliminar

#c = Categoria.objects.get(id=1)
#c.delete()
#consulta = Categoria.objects.all()
#print(consulta)

# filtrado
for c in Categoria.objects.filter():
    print(c.nombre)