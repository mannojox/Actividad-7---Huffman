from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from collections import Counter
import heapq
import os

# Nodo para el árbol de Huffman
class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia
    
# Función para calcular la frecuencia de los caracteres en un archivo
def calcular_frecuencia():
    # Pedir al usuario que seleccione un archivo
    archivo = filedialog.askopenfilename()  
    if archivo:
        # Leer el contenido del archivo y contar la frecuencia de cada carácter
        with open(archivo, 'r', encoding='utf-8') as f:  
            contenido = f.read()
            frecuencia = Counter(contenido)
            # Ordenar la lista de frecuencias en orden 
            lista_frecuencia = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)
            # Mostrar la lista de frecuencias en una nueva ventana
            mostrar_frecuencia(lista_frecuencia)

def mostrar_frecuencia(lista_frecuencia):
    ventana_frecuencia = Toplevel(root)
    ventana_frecuencia.title("Lista de Frecuencia de Caracteres")

# Crear una barra de desplazamiento
    txt_frecuencia = Text(ventana_frecuencia, wrap=NONE)
    scrollbar = Scrollbar(ventana_frecuencia, orient=VERTICAL, command=txt_frecuencia.yview)
    txt_frecuencia.config(yscrollcommand=scrollbar.set)

    # Mostrar la lista de frecuencia en el Textbox
    for item in lista_frecuencia:
        txt_frecuencia.insert(END, f"{item[0]} : {item[1]}\n")
    
    # Empacar el Textbox y la barra de desplazamiento
    txt_frecuencia.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

# Construir el árbol de Huffman
def construir_arbol(lista_frecuencia):
    heap = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in lista_frecuencia]
    heapq.heapify(heap)
    while len(heap) > 1:
        izquierda = heapq.heappop(heap)
        derecha = heapq.heappop(heap)
        nodo_padre = NodoHuffman(None, izquierda.frecuencia + derecha.frecuencia)
        nodo_padre.izquierda = izquierda
        nodo_padre.derecha = derecha
        heapq.heappush(heap, nodo_padre)
    return heap[0]

# Asignar códigos de Huffman
def asignar_codigos(nodo, codigo_actual="", tabla_codigos={}):
    if nodo is not None:
        if nodo.caracter is not None:
            tabla_codigos[nodo.caracter] = codigo_actual
        asignar_codigos(nodo.izquierda, codigo_actual + "0", tabla_codigos)
        asignar_codigos(nodo.derecha, codigo_actual + "1", tabla_codigos)
    return tabla_codigos

# Comprimir el archivo de texto
def comprimir():
    archivo_original = filedialog.askopenfilename()
    if archivo_original:
        with open(archivo_original, 'r', encoding='utf-8') as f:
            contenido = f.read()
            frecuencia = Counter(contenido)
            lista_frecuencia = sorted(frecuencia.items(), key=lambda x: x[1])
            arbol = construir_arbol(lista_frecuencia)
            tabla_codigos = asignar_codigos(arbol)
            archivo_comprimido = archivo_original + ".huf"
            with open(archivo_comprimido, 'wb') as f:
                f.write(bytes(str(tabla_codigos), 'utf-8'))
                bits = ""
                for caracter in contenido:
                    bits += tabla_codigos[caracter]
                    while len(bits) >= 8:
                        byte = bits[:8]
                        bits = bits[8:]
                        f.write(bytes([int(byte, 2)]))
                if bits:
                    bits += '0' * (8 - len(bits))
                    f.write(bytes([int(bits, 2)]))

# Descomprimir el archivo de texto
def descomprimir():
    archivo_comprimido = filedialog.askopenfilename()
    if archivo_comprimido:
        with open(archivo_comprimido, 'rb') as f:
            contenido = f.read()
            tabla_codigos = eval(contenido[:contenido.find(b'}') + 1])
            bits = ''.join(format(byte, '08b') for byte in contenido[contenido.find(b'}') + 1:])
            archivo_descomprimido = os.path.splitext(archivo_comprimido)[0]
            nodo = construir_arbol([(None, 0)])
            resultado = ""
            nodo_actual = nodo  # Guardar una copia del nodo raíz
            for bit in bits:
                if bit == '0':
                    nodo_actual = nodo_actual.izquierda
                else:
                    nodo_actual = nodo_actual.derecha
                if nodo_actual.caracter is not None:
                    resultado += nodo_actual.caracter
                    nodo_actual = nodo  # Reiniciar al nodo raíz para buscar el próximo caracter
            with open(archivo_descomprimido, 'w', encoding='utf-8') as f:
                f.write(resultado)



# Configuración de la interfaz de usuario
root = Tk()
root.title("ACT 07 - Entrega 1 Huffman")
root.geometry("400x430")

frm = ttk.Frame(root, padding=10)
frm.grid()

# Etiqueta de bienvenida
ttk.Label(frm, text="Bienvenido a tu programa de confianza para comprimir archivos").grid(column=1, row=0)

# Botones
ttk.Button(frm, text="Examinar", command=calcular_frecuencia).grid(column=1, row=1)
ttk.Button(frm, text="Comprimir", command=comprimir).grid(column=1, row=2)
ttk.Button(frm, text="Descomprimir", command=descomprimir).grid(column=1, row=3)
ttk.Button(frm, text="Salir", command=root.destroy).grid(column=1, row=4)

root.mainloop()
