import tkinter as tk

from tkinter import filedialog

import ply.lex as lex

import re

# Lista de tokens
tokens = (
    'DOCTYPE_ARTICLE',
    'OPEN_ARTICLE',
    'CLOSE_ARTICLE',
    'OPEN_SECTION',
    'CLOSE_SECTION',
    'OPEN_TITLE',
    'CLOSE_TITLE',
    'OPEN_AUTHOR',
    'CLOSE_AUTHOR',
    'OPEN_ABSTRACT',
    'CLOSE_ABSTRACT',
    'OPEN_DATE',
    'CLOSE_DATE',
    'OPEN_COPYRIGHT',
    'CLOSE_COPYRIGHT',
    'OPEN_ADDRESS',
    'CLOSE_ADDRESS',
    'OPEN_PARA',
    'CLOSE_PARA',
    'OPEN_ITEMIZEDLIST',
    'CLOSE_ITEMIZEDLIST',
    'OPEN_LISTITEM',
    'CLOSE_LISTITEM',
    'OPEN_IMPORTANT',
    'CLOSE_IMPORTANT',
    'OPEN_ROW',
    'CLOSE_ROW',
    'OPEN_ENTRY',
    'CLOSE_ENTRY',
    'OPEN_MEDIAOBJECT',
    'CLOSE_MEDIAOBJECT',
    'OPEN_IMAGENOBJECT',
    'CLOSE_IMAGENOBJECT',
    'OPEN_FIRSTNAME',
    'CLOSE_FIRSTNAME',
    'OPEN_SURNAME',
    'CLOSE_SURNAME',
    'OPEN_STREET',
    'CLOSE_STREET',
    'OPEN_PHONE',
    'CLOSE_PHONE',
    'OPEN_EMAIL',
    'CLOSE_EMAIL',
    'OPEN_YEAR',
    'CLOSE_YEAR',
    'OPEN_HOLDER',
    'CLOSE_HOLDER',
    'OPEN_EMPHASIS',
    'CLOSE_EMPHASIS',
    'OPEN_LINK',
    'CLOSE_LINK',
    'OPEN_INFORMALTABLE',
    'CLOSE_INFORMALTABLE',
    'OPEN_COMMENT',
    'CLOSE_COMMENT',
    'OPEN_SIMPLESEC',
    'CLOSE_SIMPLESEC',
    'OPEN_SIMPARA',
    'CLOSE_SIMPARA',
    'OPEN_INFO',
    'CLOSE_INFO',
    'TEXT',
    'URL',
    'OPEN_VIDEOOBJECT',
    'CLOSE_VIDEOOBJECT',
    'IMAGENDATA',
    'VIDEODATA',
    'OPEN_TGROUP',
    'CLOSE_TGROUP',
    'OPEN_THEAD',
    'CLOSE_THEAD',
    'OPEN_TFOOT',
    'CLOSE_TFOOT',
    'OPEN_ENTRYTBL',
    'CLOSE_ENTRYTBL',
    'OPEN_CITY',
    'CLOSE_CITY',
    'OPEN_STATE',
    'CLOSE_STATE',
    'OPEN_TBODY',
    'CLOSE_TBODY',
)

# Definición de patrones para los tokens


def t_DOCTYPE_ARTICLE(t):
    r'<!DOCTYPE\s+article>'
    archivo_html.write("<!DOCTYPE html>\n<html>\n<head>\n   <title>Ejemplo de Estilos en Archivo HTML</title>\n</head>\n")
    return t


def t_OPEN_ARTICLE(t):
    r'<article>'
    archivo_html.write("<body>\n    ")
    return t


def t_CLOSE_ARTICLE(t): 
    r'</article>'
    archivo_html.write("\n</body>")
    return t

t_OPEN_SECTION = r'<section>'
t_CLOSE_SECTION = r'</section>'
t_OPEN_TITLE = r'<title>'
t_CLOSE_TITLE = r'</title>'
t_OPEN_AUTHOR = r'<author>'
t_CLOSE_AUTHOR = r'</author>'
t_OPEN_ABSTRACT = r'<abstract>'
t_CLOSE_ABSTRACT = r'</abstract>'
t_OPEN_DATE = r'<date>'
t_CLOSE_DATE = r'</date>'
t_OPEN_COPYRIGHT = r'<copyright>'
t_CLOSE_COPYRIGHT = r'</copyright>'
t_OPEN_ADDRESS = r'<address>'
t_CLOSE_ADDRESS = r'</address>'
t_OPEN_ROW = r'<row>'
t_CLOSE_ROW = r'</row>'


def t_OPEN_PARA(t):
    r'<para>'
    archivo_html.write("\n<p>")
    return t

def t_CLOSE_PARA(t):
    r'</para>'
    archivo_html.write("</p>\n")
    return t

def t_OPEN_SIMPARA(t):
    r'<simpara>'
    archivo_html.write("\n<p>")
    return t

def t_CLOSE_SIMPARA(t):
    r'</simpara>'
    archivo_html.write("</p>\n")
    return t

def t_OPEN_ITEMIZEDLIST(t):
    r'<itemizedlist>'
    archivo_html.write("\n<ul>")
    return t

def t_CLOSE_ITEMIZEDLIST(t):
    r'</itemizedlist>'
    archivo_html.write("</ul>\n")
    return t

def t_OPEN_LISTITEM(t):
    r'<listitem>'
    archivo_html.write("\n<li>")
    return t

def t_CLOSE_LISTITEM(t):
    r'</listitem>'
    archivo_html.write("</li>\n")
    return t


def t_OPEN_IMPORTANT(t):
    r'<important>'
    archivo_html.write('\n<div style="background-color:red;color:white">') #anda bien
    return t


def t_CLOSE_IMPORTANT(t): 
    r'</important>'
    archivo_html.write('</div>\n')
    return t

def t_OPEN_TBODY(t):
    r'<tbody>'
    archivo_html.write("<tr>")
    return t

def t_CLOSE_TBODY(t):
    r'</tbody>'
    archivo_html.write("</tr>")
    return t

def t_OPEN_THEAD(t):
    r'<thead>'
    archivo_html.write("<th>")
    return t

def t_CLOSE_THEAD(t):
    r'</thead>'
    archivo_html.write("</th>")
    return t

def t_OPEN_TFOOT(t):
    r'<tfoot>'
    archivo_html.write("<td>")
    return t

def t_CLOSE_TFOOT(t):
    r'</tfoot>'
    archivo_html.write("</td>")
    return t




t_OPEN_MEDIAOBJECT = r'<mediaobject>'
t_CLOSE_MEDIAOBJECT = r'</mediaobject>'
t_OPEN_FIRSTNAME = r'<firstname>'
t_CLOSE_FIRSTNAME = r'</firstname>'
t_OPEN_SURNAME = r'<surname>'
t_CLOSE_SURNAME = r'</surname>'
t_OPEN_STREET = r'<street>'
t_CLOSE_STREET = r'</street>'
t_OPEN_PHONE = r'<phone>'
t_CLOSE_PHONE = r'</phone>'
t_OPEN_EMAIL = r'<email>'
t_CLOSE_EMAIL = r'</email>'
t_OPEN_YEAR = r'<year>'
t_CLOSE_YEAR = r'</year>'
t_OPEN_HOLDER = r'<holder>'
t_CLOSE_HOLDER = r'</holder>'
t_OPEN_EMPHASIS = r'<emphasis>'
t_CLOSE_EMPHASIS = r'</emphasis>'

def t_OPEN_LINK(t):
    r'<link\s+xlink:href\s*=\s*"([^"]*)"\s*/?>' 
    pattern = r'<link\s+xlink:href\s*=\s*"([^"]*)"\s*/?>'  # Patrón con expresión regular
    match = re.search(pattern, t.value) 
    if match:
        url = match.group(1)  # Obtener el valor entre las comillas dobles
    else:
        url=''
    archivo_html.write(f"<a href='{url}'>")
    return t


def t_CLOSE_LINK(t):
      r'</link>'
      archivo_html.write("</a>")
      return t

def t_OPEN_INFORMALTABLE(t):
    r'<informaltable>'
    archivo_html.write("\n<table>")
    return t

def t_CLOSE_INFORMALTABLE(t):
    r'</informaltable>'
    archivo_html.write("</table>  ")
    return t

t_OPEN_COMMENT = r'<comment>'
t_CLOSE_COMMENT = r'</comment>'
t_OPEN_SIMPLESEC = r'<simplesec>'
t_CLOSE_SIMPLESEC = r'</simplesec>'

def t_OPEN_INFO(t):
    r'<info>'
    archivo_html.write('\n<div style="color:white;background-color:green;font-size:8pts">')   #anda bien
    return t


def t_CLOSE_INFO(t):
    r'</info>'
    archivo_html.write('</div>')
    return t


def t_TEXT(t):
    r'[^<>!/]+'
    archivo_html.write(f'{t.value}')
    return (t)



t_OPEN_IMAGENOBJECT = r'<imageobject>'
t_CLOSE_IMAGENOBJECT = r'</imageobject>'
t_OPEN_VIDEOOBJECT = r'<videoobject>'
t_CLOSE_VIDEOOBJECT = r'</videoobject>'
t_OPEN_TGROUP = r'<tgroup>'
t_CLOSE_TGROUP = r'</tgroup>'
t_OPEN_ENTRYTBL = r'<entrytbl>'
t_CLOSE_ENTRYTBL = r'</entrytbl>'
t_OPEN_ENTRY = r'<entry>'
t_CLOSE_ENTRY = r'</entry>'
t_OPEN_CITY = r'<city>'
t_CLOSE_CITY = r'</city>'
t_OPEN_STATE = r'<state>'
t_CLOSE_STATE = r'</state>'
t_IMAGENDATA = r'<imagedata\s+url="[^"]*"\s*/>'
t_VIDEODATA = r'<videodata\s+url="[^"]*"\s*/>'

def t_URL(t):
    r'https?://[^\s<>"]+'


# Ignorar espacios en blanco y saltos de línea, r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'


t_ignore = ' \n'

#Función para manejar errores de tokens no válidos

def t_error(t):    
	print ("caracter ilegal %s" % t.value[0])
	t.lexer.skip(1)

# Crear el lexer

archivo_html = open("HTML_Salida.html", "w")

lexer = lex.lex()




def open_file():
    selected_file = filedialog.askopenfilename(filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    label = tk.Label(window, text="Archivo seleccionado: " + selected_file)
    label.pack()
    
    def run_lexer():
        with open(selected_file, 'r') as file:
            data = file.read()
        lexer.input(data)
        error = False

        while True:
            token = lexer.token()
            print(token)
            if token is None:
                break
            elif token.value == "true":
                error = True

        if error:
            label = tk.Label(window, text="El lenguaje tiene un error en...")  # Debes especificar en qué parte hay un error
        else:
            label = tk.Label(window, text="¡Lenguaje escrito correctamente!")
        label.pack()

    execute_button = tk.Button(window, text="Ejecutar", state=tk.NORMAL, command=run_lexer)
    execute_button.pack()

def show_input_window():
    def run_lexer():
        data = input_text.get()
        lexer.input(data)
        error = False

        while True:
            token = lexer.token()
            print(token)
            if token is None:
                break
            elif token.value == "true":
                error = True

        if error:
            label = tk.Label(input_window, text="El lenguaje tiene un error en...")  # Debes especificar en qué parte hay un error
        else:
            label = tk.Label(input_window, text="¡Lenguaje escrito correctamente!")
        label.pack()
        

    input_window = tk.Toplevel(window)
    input_window.title("Ventana de Entrada")
    input_window.geometry("800x400")
    
    input_label = tk.Label(input_window, text="Ingrese un texto")
    input_label.pack()
    
    input_text = tk.Entry(input_window)
    input_text.pack()

    execute_button = tk.Button(input_window, text="Ejecutar", state=tk.NORMAL, command=run_lexer)
    execute_button.pack()
    
    exit_button = tk.Button(input_window, text="Salir", command=input_window.destroy)
    exit_button.pack()

def close_interface(event):
    if event.keysym == 'd' and event.state == 4:  # Comprueba si se presionó Control + D
        window.quit()

# Crear la ventana principal
window = tk.Tk()
window.title("Analizador Lexico DOCBOOK")
window.geometry("800x400")

# Crear los elementos de la interfaz
label = tk.Label(window, text="Presiona el botón 'Archivo de Lectura' para seleccionar un archivo de lectura del parser.\nPresiona el botón 'Modo Interactivo' para ingresar el texto del deseas realizar la comprobacion sintatica.")
label.pack()

button1 = tk.Button(window, text="Archivo de Lectura", command=open_file)
button1.pack()

button2 = tk.Button(window, text="Modo Interactivo", command=show_input_window)
button2.pack()

exit_button = tk.Button(window, text="Salir", command=window.quit)
exit_button.pack()

# Vincular el cierre de la interfaz a la combinación de teclas Control + D
window.bind('<Control-d>', close_interface)

# Iniciar el bucle principal de la ventana
window.mainloop()