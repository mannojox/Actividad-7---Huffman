import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    print("Archivo seleccionado:", ruta_archivo)

#ventana
ventana = tk.Tk()
ventana.title("Participacion Huffman - Ventana")

#tamaño de la ventana
ventana.geometry("400x300")  # pixeles ancho x alto

#botones
boton_examinar = tk.Button(ventana, text="Examinar", command=seleccionar_archivo)
boton_examinar.pack(pady=10)

boton_comprimir = tk.Button(ventana, text="Comprimir")
boton_comprimir.pack(pady=10)

boton_descomprimir = tk.Button(ventana, text="Descomprimir")
boton_descomprimir.pack(pady=10)


ventana.mainloop()

