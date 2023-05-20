import ply.lex as lex

# Lista de tokens
tokens = (
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
    'TEXT',
)

# Definición de patrones para los tokens
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
t_TEXT = r'[^<>]+'

# Ignorar espacios en blanco y salt
