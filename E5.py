from arbol_binario import Arbol

#  Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
#  se (MCU), desarrollar un algoritmo que contemple lo siguiente:
#  a.además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
#  leano que indica si es un héroe o un villano, True y False respectivamente;
#  b.listar los villanos ordenados alfabéticamente;
#  c.mostrar todos los superhéroes que empiezan con C;
#  d.determinar cuántos superhéroes hay el árbol;
#  e.Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#  encontrarlo en el árbol y modificar su nombre;
#  f.listar los superhéroes ordenados de manera descendente;
#  g.generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#  los villanos, luego resolver las siguiente tareas:


MCU = [
    {'nombre' : 'Iron Man', 'heroe' : True},
    {'nombre' : 'Spider Man', 'heroe' : True},
    {'nombre' : 'Hulk', 'heroe' : True},
    {'nombre' : 'Thanos', 'heroe' : False},
    {'nombre' : 'Dr. Strange', 'heroe' : True},
    
]

arbolMCU = Arbol()

for personaje in MCU:
    arbolMCU= arbolMCU.insertar_nodo(personaje['nombre'], personaje)


#  Ejercicio b
arbolMCU.inorden()

#  Ejercicio c
arbolMCU.busqueda_proximidad('C')

#  ejercicio d
print(arbolMCU.contar_nodos())

#  ejercicio e
arbolMCU.inorden()
arbolMCU.remplazar_proximidad_MCU('Dr', 'Dr. Strange')
arbolMCU.inorden()

#  ejercicio f
arbolMCU.postorden()

#  ejercicio g
arbol_villanos = Arbol()
arbol_heroes = Arbol()

arbolMCU.separarHyV(arbol_heroes,arbol_villanos)

print('Arbol de heroes')
arbol_heroes.inorden()

print('Arbol de villanos')
arbol_villanos.inorden()

arbol_heroes.balancear()
arbol_villanos.balancear()
