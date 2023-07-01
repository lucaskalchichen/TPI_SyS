
import argparse

import ply.lex as lex





# Lista de tokens
tokens = (
    'DOCTYPE_ARTICLE',
    'OPEN_ARTICLE',
    'CLOSE_ARTICLE',
    'OPEN_BOOK',
    'CLOSE_BOOK',
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
    'OPEN_ORDEREDLIST',
    'CLOSE_ORDEREDLIST',
    'OPEN_UNORDEREDLIST',
    'CLOSE_UNORDEREDLIST',
    'OPEN_LISTITEM',
    'CLOSE_LISTITEM',
    'OPEN_IMPORTANT',
    'CLOSE_IMPORTANT',
    'OPEN_TABLE',
    'CLOSE_TABLE',
    'OPEN_ROW',
    'CLOSE_ROW',
    'OPEN_ENTRY',
    'CLOSE_ENTRY',
    'OPEN_FIGURE',
    'CLOSE_FIGURE',
    'OPEN_MEDIAOBJECT',
    'CLOSE_MEDIAOBJECT',
    'OPEN_IMAGEOBJECT',
    'CLOSE_IMAGEOBJECT',
    'OPEN_IMAGEDATA',
    'CLOSE_IMAGEDATA',
    'OPEN_PROGRAMLISTING',
    'CLOSE_PROGRAMLISTING',
    'OPEN_NOTE',
    'CLOSE_NOTE',
    'OPEN_FIRSTNAME',
    'CLOSE_FIRSTNAME',
    'OPEN_SURNAME',
    'CLOSE_SURNAME',
    'OPEN_TEXTO',
    'CLOSE_TEXTO',
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
    'XLINK_ATTRIBUTE',
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
    'OPEN_IMAGENOBJECT',
    'CLOSE_IMAGENOBJECT',
    'IMAGENDATA',
    'VIDEODATA',
)

# Definición de patrones para los tokens
t_DOCTYPE_ARTICLE = r"<!DOCTYPE\s+article>"
t_OPEN_ARTICLE = r'<article>'
t_CLOSE_ARTICLE = r'</article>'
t_OPEN_BOOK = r'<book>'
t_CLOSE_BOOK = r'</book>'
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
t_OPEN_PARA = r'<para>'
t_CLOSE_PARA = r'</para>'
t_OPEN_ORDEREDLIST = r'<orderedlist>'
t_CLOSE_ORDEREDLIST = r'</orderedlist>'
t_OPEN_UNORDEREDLIST = r'<itemizedlist>'
t_CLOSE_UNORDEREDLIST = r'</itemizedlist>'
t_OPEN_LISTITEM = r'<listitem>'
t_CLOSE_LISTITEM = r'</listitem>'
t_OPEN_IMPORTANT = r'<important>'
t_CLOSE_IMPORTANT = r'</important>'
t_OPEN_TABLE = r'<table>'
t_CLOSE_TABLE = r'</table>'
t_OPEN_ROW = r'<row>'
t_CLOSE_ROW = r'</row>'
t_OPEN_ENTRY = r'<entry>'
t_CLOSE_ENTRY = r'</entry>'
t_OPEN_FIGURE = r'<figure>'
t_CLOSE_FIGURE = r'</figure>'
t_OPEN_MEDIAOBJECT = r'<mediaobject>'
t_CLOSE_MEDIAOBJECT = r'</mediaobject>'
t_OPEN_IMAGEOBJECT = r'<imageobject>'
t_CLOSE_IMAGEOBJECT = r'</imageobject>'
t_OPEN_IMAGEDATA = r'<imagedata>'
t_CLOSE_IMAGEDATA = r'</imagedata>'
t_OPEN_PROGRAMLISTING = r'<programlisting>'
t_CLOSE_PROGRAMLISTING = r'</programlisting>'
t_OPEN_NOTE = r'<note>'
t_CLOSE_NOTE = r'</note>'
t_OPEN_FIRSTNAME = r'<firstname>'
t_CLOSE_FIRSTNAME = r'</firstname>'
t_OPEN_SURNAME = r'<surname>'
t_CLOSE_SURNAME = r'</surname>'
t_OPEN_TEXTO = r'<texto>'
t_CLOSE_TEXTO = r'</texto>'
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
#t_OPEN_LINK = r'<link>'
t_CLOSE_LINK = r'</link>'
t_OPEN_INFORMALTABLE = r'<informaltable>'
t_CLOSE_INFORMALTABLE = r'</informaltable>'
t_OPEN_COMMENT = r'<comment>'
t_CLOSE_COMMENT = r'</comment>'
t_OPEN_SIMPLESEC = r'<simplesec>'
t_CLOSE_SIMPLESEC = r'</simplesec>'
t_OPEN_SIMPARA = r'<simpara>'
t_CLOSE_SIMPARA = r'</simpara>'
t_OPEN_INFO = r'<info>'
t_CLOSE_INFO = r'</info>'
t_TEXT = r'[^<>!]+'
t_OPEN_IMAGENOBJECT =r'<imageobject>'
t_CLOSE_IMAGENOBJECT =r'</imageobject>'
t_OPEN_VIDEOOBJECT =r'<videoobject>'
t_CLOSE_VIDEOOBJECT =r'</videoobject>'

def t_VIDEODATA(t):
    t.value = t.lexer.lexmatch.group('URL')
    return t
t_VIDEODATA.__doc__ = r'<videodata\s+fileref="{URL}"/>'.format(URL=r'https?://[^\s<>"]+')

def t_IMAGENDATA(t):
    t.value = t.lexer.lexmatch.group('URL')
    return t
t_IMAGENDATA.__doc__ = r'<imagedata\s+fileref="{URL}"/>'.format(URL=r'https?://[^\s<>"]+')

def t_OPEN_LINK(t):
    t.value = t.lexer.lexmatch.group('URL')
    return t
t_OPEN_LINK.__doc__ = r'<openlink\s+url="{URL}"/>'.format(URL=r'https?://[^\s<>"]+')

def t_URL(p):
   r'https?://[^\s<>"]+'
   return t

# Ignorar espacios en blanco y saltos de línea, r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'


t_ignore = ' \n'

# Función para manejar errores de tokens no válidos
'''def t_error(t):
    if t.value.startswith('<') and t.value.endswith('>'):
        print("Etiqueta no válida: '%s'" % t.value)
    else:
        print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)
'''

def t_error(t):
    if t.value.startswith('<') and t.value.endswith('>'):
        print("Etiqueta no válida: '%s'" % t.value)
    else:
        print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()

data = '''
<!DOCTYPE article>
    <article>
        <info>
            <title>El titulo del articulo</title>
            <author>
                <firstname>Juan</firstname>
                <surname>Perez</surname>
            </author>
        </info>
        <section>
            <title>Titulo para la seccion 1</title>
            <para>
                Esto es un parrafo
            </para>
            <para>
                Otro parrafo.
            </para>
        </section>
    </article>
'''


# Asignar la cadena de entrada al lexer
lexer.input(data)

# Probar el lexer
while True:
    token = lexer.token()
    if not token:
        break
    print(token)
