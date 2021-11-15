"""Una empresa de nano satélites dedicada al monitoreo de lotes campo destinados al agro, tiene
problemas para la transmisión de los datos recolectados, dado que la ventana de tiempo que
dispone para enviar los datos antes de una nueva medición es muy corta, por lo que nos solicita

desarrollar un algoritmo que permita comprimir la información para poder enviarla más rápi-
do, para lo cual se debe tener en cuenta los siguientes requerimientos:

a. la información transmitida por el nano satélite son estado del tiempo, humedad del suelo,
y tres dígitos que identifican el lote al cual pertenecen los datos;
b. desarrollar un árbol de Huffman que permita comprimir la información para transmitirla,
la frecuencia de la información transmitida se observa en la siguiente tabla:

c. comprimir un mensaje y descomprimirlo, para ver si no se pierde información durante el
proceso de codificación, la trama enviada por el nano satélite tiene el siguiente formato
(estado del clima-humedad del suelo-cod1-cod2-cod3), por ejemplo la siguiente trama es
válida “Nublado-Baja-1-5-7”, –los guiones son a fines de comprender como está formada la
trama pero no forman parte de la misma–;
d. determinar la diferencia en tamaño de memoria utilizada por la trama original y la trama
comprimida –puede utilizar la función getsizeof() de la librería sys–."""

from arbol_binario import Arbol
from cola import Cola

tabla = [['Despejado', 0.22], ['Nublado', 0.15], ['Lluvia', 0.03], ['Baja', 0.26], ['Alta', 0.14], ['1', 0.05], ['2', 0.01], ['3', 0.035], ['5', 0.06], ['7', 0.02], ['8', 0.25]]

dic = {}


def como_comparo(arbol):
    return arbol.frecuencia


bosque = []

for info, frecuencia in tabla:
    arbol = Arbol(info, frecuencia = frecuencia)
    bosque.append(arbol)


bosque.sort(key=como_comparo)


while(len(bosque) > 1):
    arbol1 = bosque.pop(0)
    arbol2 = bosque.pop(0)
    nuevo_arbol = Arbol(frecuencia=arbol1.frecuencia+arbol2.frecuencia)
    nuevo_arbol.izq = arbol1
    nuevo_arbol.der = arbol2
    bosque.append(nuevo_arbol)
    bosque.sort(key=como_comparo)

arbol_huffman = bosque[0]

arbol_huffman.barrido_por_nivel_huff()
print()

def generar_tabla(arbol, cadena='', dic=None):
    if(arbol is not None):
        if(arbol.izq is None):
            dic[arbol.info] = cadena
        else:
            cadena += '0'
            generar_tabla(arbol.izq, cadena, dic)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(arbol.der, cadena, dic)


generar_tabla(arbol_huffman, dic=dic)


def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena:
        cadena_cod += dic[caracter]
    return cadena_cod


def decodificar(cadena_cod, arbol_huff):
    cadena_deco = ''
    arbol_aux = arbol_huff
    pos = 0
    while(pos < len(cadena_cod)):
        if(cadena_cod[pos] == '0'):
            arbol_aux = arbol_aux.izq
        else:
            arbol_aux = arbol_aux.der
        pos += 1
        if(arbol_aux.izq is None):
            cadena_deco += arbol_aux.info
            arbol_aux = arbol_huff
    return cadena_deco


cadena = ["Nublado","Baja","1","5","7"]
cadena_cod = codificar(cadena, dic)

print("Cadena codificada: ")
print(cadena_cod)
print("Cadena decodificada:")
print(decodificar(cadena_cod, arbol_huffman))

from sys import getsizeof
print(getsizeof(cadena_cod), getsizeof(b'1010111001110101101111'))