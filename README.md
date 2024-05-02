# Actividad-7---Huffman
En este repositorio se subirán los archivos de la actividad 7 (Huffman)

Desarrollo
La codificación de Huffman básicamente funciona de la siguiente manera:
•	Cálculo de frecuencias: Primero, se calcula la frecuencia de cada carácter en los datos que se van a comprimir. Esto implica contar cuántas veces aparece cada carácter en el archivo o mensaje.
•	Construcción del árbol de Huffman: Se utiliza la información de frecuencia para construir un árbol de Huffman. Este árbol es un árbol binario donde cada hoja representa un carácter y la ruta desde la raíz hasta una hoja determina el código de Huffman para ese carácter. Los caracteres más frecuentes se colocan en niveles más bajos del árbol, lo que resulta en códigos más cortos.
•	Generación de códigos: A partir del árbol de Huffman construido, se generan los códigos de Huffman para cada carácter. Los códigos se forman siguiendo el camino desde la raíz del árbol hasta cada hoja. Por ejemplo, un camino hacia la izquierda puede representar un 0 y un camino hacia la derecha representa un 1.
•	Compresión: Una vez que se han generado los códigos de Huffman, se utiliza esta información para comprimir los datos originales. Cada carácter en los datos se reemplaza por su correspondiente código de Huffman. Como los códigos de Huffman para caracteres comunes son más cortos, la longitud total de los datos comprimidos suele ser menor que la longitud de los datos originales.
•	Descompresión: Para recuperar los datos originales a partir de los datos comprimidos, se utiliza el árbol de Huffman. Se recorre el árbol según los bits en los datos comprimidos hasta alcanzar una hoja, que corresponde a un carácter en los datos originales.
Observaciones del front-end:
CRISTIAN CHAVEZ VELASCO fue la persona que me envió su front-end. Su programa hace uso de las librerías tkinter para la interfaz gráfica y collections para ayudar en la función calcular_frecuencia.
El programa tiene las siguientes funciones:
•	calcular_frecuencia(): Lo primero que hace esta función es abrir el explorador de archivos con filedialog.askopenfilename(). Después lee el archivo seleccionado en modo lectura ‘r’ y guarda el texto en una variable “contenido”. Posteriormente utiliza Counter de la librería collections para guardar el conteo de los caracteres de “contenido”. Counter es una subclase de dict que sirve para contar, es una colección en la cual los elementos son almacenados como llaves del diccionario y sus cantidades son almacenadas como valores del diccionario. Finalmente esta función ordena los elementos de mayor a menor en base a la cantidad de veces que se repiten, para lograr esto usa sorted.
•	mostrar_frecuencia(lista_frecuencia): Esta función recibe la lista de frecuencias como parámetro y la despliega en un widget de texto de tkinter.
Aparte de estas funciones, el código contiene los demás elementos necesarios para que el front-end funcione correctamente, como la ventana principal, los botones, labels, etc. Es una interfaz gráfica básica pero completamente funcional.

