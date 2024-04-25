def caracteresRepeticiones(archivo):
    repeticiones = {}
    with open(archivo, 'r') as file:
        texto = file.read()
        for car in texto:
             if car in repeticiones:
                    repeticiones[car] += 1
             else: 
                    repeticiones[car] = 1

    return repeticiones

# ejemplo:
archivo = "prueba.txt"
           
resultado = caracteresRepeticiones(archivo)
print(resultado)


