import tkinter as tk
from tkinter import filedialog


def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    etiqueta.config(text="Archivo seleccionado: " + archivo)
    boton_ejecutar.config(state=tk.NORMAL)

def mostrar_ventana_entrada():
    ventana_entrada = tk.Toplevel(ventana)
    ventana_entrada.title("Ventana de Entrada")
    ventana_entrada.geometry("400x200")
    
    etiqueta_entrada = tk.Label(ventana_entrada, text="Ingrese un texto")
    etiqueta_entrada.pack()
    
    entrada_texto = tk.Entry(ventana_entrada)
    entrada_texto.pack()
    
    boton_ejecutar_entrada = tk.Button(ventana_entrada, text="Ejecutar" ,command=)
    boton_ejecutar_entrada.pack()
    
    boton_salir_entrada = tk.Button(ventana_entrada, text="Salir", command=ventana_entrada.destroy)
    boton_salir_entrada.pack()

def cerrar_interfaz(event):
    if event.keysym == 'd' and event.state == 4:  # Comprueba si se presionó Control + D
        ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz con selección de archivo")
ventana.geometry("800x400")

# Crear los elementos de la interfaz
etiqueta = tk.Label(ventana, text="Presiona el botón 'Archivo de Lectura' para seleccionar un archivo de lectura del parser.\nPresiona el botón 'Modo Interactivo' para ingresar el texto del deseas realizar la comprobacion sintatica.")
etiqueta.pack()

boton1 = tk.Button(ventana, text="Archivo de Lectura", command=abrir_archivo)
boton1.pack()

boton2 = tk.Button(ventana, text="Modo Interactivo", command=mostrar_ventana_entrada)
boton2.pack()

boton_ejecutar = tk.Button(ventana, text="Ejecutar", state=tk.DISABLED)
boton_ejecutar.pack()

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack()

# Vincular el cierre de la interfaz a la combinación de teclas Control + D
ventana.bind('<Control-d>', cerrar_interfaz)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
