from lexer.lexer import tokens

import ply.yacc as yacc

# reglas Gramaticales

def p_document(p):
    '''document : doctype article'''
def doctype(p):
    'doctype : DOCTYPE_ARTICLE'  
def p_article(p):
    '''
        article : OPEN_INFO info CLOSE_INFO article1
            |   article1
    '''

def p_article1(p):
    '''
        article1 :  OPEN_TITLE title ClOSE_TITLE article2
        article1 :  article2
    '''
def p_article2(p):
    '''
        article2 : OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST article2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT article2
            |   OPEN_PARA  para CLOSE_PARA article2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA article2
            |   OPEN_ADDRESS address CLOSE_ADDRESS article2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT article2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE article2
            |   OPEN_COMMENT TEXT CLOSE_COMMENT article2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT article2
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDRESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST article3section
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT article3section
            |   OPEN_PARA para CLOSE_PARA article3section
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA article3section
            |   OPEN_ADDRESS address CLOSE_ADDRESS article3section
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT article3section
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE article3section
            |   OPEN_COMMENT TEXT CLOSE_COMMENT article3section
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT article3section
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST article3simsection
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT article3simsection
            |   OPEN_PARA para CLOSE_PARA article3simsection
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA article3simsection
            |   OPEN_ADDRESS address CLOSE_ADDRESS article3simsection
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT article3simsection
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE article3simsection
            |   OPEN_COMMENT TEXT CLOSE_COMMENT article3simsection
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT article3simsection
    '''

def p_article3section(p):
    '''
        article3section :  OPEN_SECTION section CLOSE_SECTION article3section
        |   OPEN_SECTION section CLOSE_SECTION
    '''
def p_article3simsection(p):
    '''
    article3simsection: OPEN_SIMPLESECT simplesect CLOSE_SIMPLESECT article3simsection
    | OPEN_SIMPLESECT simplesect CLOSE_SIMPLESECT
    '''

def p_section(p):
    '''
        section : OPEN_INFO info CLOSE_INFO section1
            |   section1
    '''


def p_section1(p):
    '''
        section1 :  OPEN_TITLE title ClOSE_TITLE section2
            |   section 2
    '''

def p_section2(p):
    '''
        section2 : OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST section2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT section2
            |   OPEN_PARA  para CLOSE_PARA section2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA section2
            |   OPEN_ADDRESS address CLOSE_ADDRESS section2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT section2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE section2
            |   OPEN_COMMENT TEXT CLOSE_COMMENT section2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT section2
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDRESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST section3section
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT section3section
            |   OPEN_PARA para CLOSE_PARA section3section
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA section3section
            |   OPEN_ADDRESS address CLOSE_ADDRESS section3section
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT section3section
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE section3section
            |   OPEN_COMMENT TEXT CLOSE_COMMENT section3section
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT section3section
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST section3simsection
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT section3simsection
            |   OPEN_PARA para CLOSE_PARA section3simsection
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA section3simsection
            |   OPEN_ADDRESS address CLOSE_ADDRESS section3simsection
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT section3simsection
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE section3simsection
            |   OPEN_COMMENT TEXT CLOSE_COMMENT section3simsection
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT section3simsection
    '''

def p_section3section(p):
    '''
    section3section :  OPEN_SECTION section CLOSE_SECTION section3section
        |   OPEN_SECTION section CLOSE_SECTION
    '''

def p_section3simsection(p):
    '''
    section3simsection: OPEN_SIMPLESEC simplesec CLOSE_SIMPLESEC section3simsection
        | OPEN_SIMPLESEC simplesec CLOSE_SIMPLESEC
    '''

def p_simplesec(p):
    '''
        simplesec : OPEN_INFO info CLOSE_INFO simplesec1
            |   simplesec1
    '''


def p_simplesec1(p):
    '''
        simplesec1 :  OPEN_TITLE title ClOSE_TITLE simplesec2
            |   simplesec2
    '''

def p_simplesec2(p):
    '''
        simplesec2 : OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST simplesec2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT simplesec2
            |   OPEN_PARA  para CLOSE_PARA simplesec2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA simplesec2
            |   OPEN_ADDRESS address CLOSE_ADDRESS simplesec2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT simplesec2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE simplesec2
            |   OPEN_COMMENT TEXT CLOSE_COMMENT simplesec2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT simplesec2
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDRESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
    '''

def p_info(p):
     '''
        info : OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT info
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT info
            |   OPEN_ADDRESS address CLOSE_ADDRESS info
            |   OPEN_AUTHOR author CLOSE_AUTHOR info
            |   OPEN_DATE date CLOSE_DATE info
            |   OPEN_COPYRIGHT copyright CLOSE_COPYRIGHT info
            |   OPEN_TITLE title CLOSE_TITLE info
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
            |   OPEN_ADDRESS address CLOSE_ADDRESS 
            |   OPEN_AUTHOR author CLOSE_AUTHOR 
            |   OPEN_DATE date CLOSE_DATE 
            |   OPEN_COPYRIGHT copyright CLOSE_COPYRIGHT 
            |   OPEN_TITLE title CLOSE_TITLE
    '''

def p_abstract(p):
    '''
        abstract : OPEN_TITLE title CLOSE_TITLE abstract2
            |   abstract2 
    '''

def p_abstract2(p):
    '''
        abstract2 : OPEN_PARA para CLOSE_PARA abstract2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA abstract2
            |   OPEN_PARA para CLOSE_PARA 
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA 
    '''

def p_author(p):
    '''
        author : OPEN_FIRSTNAME firstname CLOSE_FIRSTNAME author
            |   OPEN_SURNAME surname CLOSE_SURNAME author
            |   OPEN_FIRSTNAME firstname CLOSE_FIRSTNAME 
            |   OPEN_SURNAME simpara CLOSE_SURNAME
    '''

def p_address(p):
    '''
        address : text address
            |   OPEN_STREET street CLOSE_STREET address
            |   OPEN_CITY city CLOSE_CITY address
            |   OPEN_STATE state CLOSE_STATE address
            |   OPEN_PHONE phone CLOSE_PHONE address
            |   OPEN_EMAIL email CLOSE_EMAIL address
            |   text 
            |   OPEN_STREET street CLOSE_STREET 
            |   OPEN_CITY city CLOSE_CITY 
            |   OPEN_STATE state CLOSE_STATE 
            |   OPEN_PHONE phone CLOSE_PHONE 
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   empty
    '''



def p_copyright(p):
    '''
        copyright : OPEN_YEAR year CLOSE_YEAR copyright
            |   OPEN_YEAR year CLOSE_YEAR
            |   OPEN_YEAR year CLOSE_YEAR copyright2
    '''

def p_copyright2(p):
     '''
        copyright2 : OPEN_HOLDER holder CLOSE_HOLDER copyright2
            |   OPEN_HOLDER holder CLOSE_HOLDER
    '''

def p_title(p):
   '''
        title : OPEN_TEXT text CLOSE_TEXT title
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS title
            |   link title
            |   OPEN_EMAIL email CLOSE_EMAIL title
            |   OPEN_TEXT text CLOSE_TEXT
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   link
            |   OPEN_EMAIL email CLOSE_EMAIL

    '''
    
def p_simpara(p):
    '''
    simpara : text simpara
            |   OPEN_LINK link CLOSE_LINK simpara
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS simpara
            |   OPEN_EMAIL email CLOSE_EMAIL simpara
            |   OPEN_AUTHOR author CLOSE_AUTHOR  simpara
            |   OPEN_COMMENT comment CLOSE_COMMENT simpara
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   OPEN_AUTHOR author CLOSE_AUTHOR  
    '''


def p_link(p):
    '''
    link : text link
            |   OPEN_LINK link CLOSE_LINK link
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS link
            |   OPEN_EMAIL email CLOSE_EMAIL link
            |   OPEN_AUTHOR author CLOSE_AUTHOR  link
            |   OPEN_COMMENT comment CLOSE_COMMENT link
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   OPEN_AUTHOR author CLOSE_AUTHOR  
    '''

def p_emphasis(p):
    '''
    emphasis : text emphasis
            |   OPEN_LINK link CLOSE_LINK emphasis
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS emphasis
            |   OPEN_EMAIL email CLOSE_EMAIL emphasis
            |   OPEN_AUTHOR author CLOSE_AUTHOR  emphasis
            |   OPEN_COMMENT comment CLOSE_COMMENT emphasis
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   OPEN_AUTHOR author CLOSE_AUTHOR  
    '''

def p_comment(p):
    '''
    comment : text comment
            |   OPEN_LINK link CLOSE_LINK comment
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS comment
            |   OPEN_EMAIL email CLOSE_EMAIL comment
            |   OPEN_AUTHOR author CLOSE_AUTHOR  comment
            |   OPEN_COMMENT comment CLOSE_COMMENT comment
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   OPEN_AUTHOR author CLOSE_AUTHOR  
    '''
def para(p):
    '''
            para : text para
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS para
            |   OPEN_LINK link CLOSE_LINK para
            |   OPEN_EMAIL email CLOSE_EMAIL para
            |   OPEN_AUTHOR author CLOSE_AUTHOR para
            |   OPEN_COMMENT comment CLOSE_COMMENT para
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST para
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT para
            |   OPEN_ADDRESS address CLOSE_ADDRESS para
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT para
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE para
            |   text
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_LINK link CLOSE_LINK 
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   OPEN_AUTHOR author CLOSE_AUTHOR 
            |   OPEN_COMMENT comment CLOSE_COMMENT 
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT 
            |   OPEN_ADDRESS address CLOSE_ADDRESS 
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE 
        
    '''





def p_important(p):
     '''
        important : OPEN_TITLE title CLOSE_TITLE important2
            |   important2

    '''

def p_important2(p):
     '''
        important2 : OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST important2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT important2
            |   OPEN_PARA para CLOSE_PARA important2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA important2
            |   OPEN_ADDRESS address CLOSE_ADDRESS important2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT important2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE important2
            |   OPEN_COMMENT TEXT CLOSE_COMMENT important2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT important2
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDRESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT

    '''
def p_firstname(p):
    '''
        firstname : OPEN_TEXT text CLOSE_TEXT firstname
            |   link firstname
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS firstname
            |   OPEN_COMMENT TEXT CLOSE_COMMENT firstname
            |   OPEN_TEXT text CLOSE_TEXT
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
    '''
def p_surname(p):
    '''
        surname : OPEN_TEXT text CLOSE_TEXT surname
            |   link surname
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS surname
            |   OPEN_COMMENT TEXT CLOSE_COMMENT surname
            |   OPEN_TEXT text CLOSE_TEXT
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
    '''
def p_street(p):
     '''
        street : OPEN_TEXT text CLOSE_TEXT street
            |   link street
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS street
            |   OPEN_COMMENT TEXT CLOSE_COMMENT street
            |   OPEN_TEXT text CLOSE_TEXT
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
    '''
def p_city(p):
    '''
        city : OPEN_TEXT text CLOSE_TEXT city
            |   link city
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS city
            |   OPEN_COMMENT TEXT CLOSE_COMMENT city
            |   OPEN_TEXT text CLOSE_TEXT
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
    '''
def p_state(p):
    '''
        state : OPEN_TEXT text CLOSE_TEXT state
            |   link state
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS state
            |   OPEN_COMMENT TEXT CLOSE_COMMENT state
            |   OPEN_TEXT text CLOSE_TEXT
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
    '''
def p_phone(p):
     '''
        phone : OPEN_TEXT text CLOSE_TEXT phone
            |   link phone
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS phone
            |   OPEN_COMMENT TEXT CLOSE_COMMENT phone
            |   OPEN_TEXT text CLOSE_TEXT
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
    '''
def p_email(p):
    '''
        email : OPEN_TEXT text CLOSE_TEXT email
            |   link email
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS email
            |   OPEN_COMMENT TEXT CLOSE_COMMENT email
            |   OPEN_TEXT text CLOSE_TEXT
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
    '''
def p_date(p):
    '''
        date : OPEN_TEXT text CLOSE_TEXT date
            |   link date
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS date
            |   OPEN_COMMENT TEXT CLOSE_COMMENT date
            |   OPEN_TEXT text CLOSE_TEXT
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
    '''
def p_year(p):
     '''
        year : OPEN_TEXT text CLOSE_TEXT year
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS year
            |   OPEN_COMMENT TEXT CLOSE_COMMENT year
            |   OPEN_TEXT text CLOSE_TEXT
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
    '''
def p_holder(p):
    '''
        holder : OPEN_TEXT text CLOSE_TEXT holder
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS holder
            |   OPEN_COMMENT TEXT CLOSE_COMMENT holder
            |   OPEN_TEXT text CLOSE_TEXT
            |   link
            |   OPEN_EMPHASIS TEXT CLOSE_EMPHASIS
            |   OPEN_COMMENT TEXT CLOSE_COMMENT
    '''

def p_link(p):
    '''
    link : OPEN_LINK TEXT CLOSE_LINK
    '''
def p_mediaobject(p):
     '''
        mediaobject : OPEN_INFO info CLOSE_INFO mediadata
            |   mediadata
    '''
def p_mediadata(p):
     '''
        mediadata : OPEN_VIDEOOBJECT videoobject CLOSE_VIDEOOBJECT mediadata2
            |  OPEN_IMAGENOBJECT imageobject CLOSE_IMAGENOBJECT mediadata3
            |  OPEN_VIDEOOBJECT videoobject CLOSE_VIDEOOBJECT
            |  OPEN_IMAGENOBJECT imageobject CLOSE_IMAGENOBJECT
    '''
def p_mediadata2(p):
     '''
        mediadata2 : OPEN_VIDEOOBJECT videoobject CLOSE_VIDEOOBJECT mediadata2
            |   OPEN_IMAGENOBJECT imageobject CLOSE_IMAGENOBJECT mediadata2
    '''
def p_mediadata3(p):
     '''
        mediadata3 : OPEN_VIDEOOBJECT videoobject CLOSE_VIDEOOBJECT mediadata3
            |   OPEN_IMAGENOBJECT imageobject CLOSE_IMAGENOBJECT mediadata3
    '''
def p_videoobject(p):
    '''
        videoobject : OPEN_INFO INFO CLOSE_INFO videoobject2
            |   videoobject2
    '''
def p_imageobject(p):
    '''
        imageobject : OPEN_INFO INFO CLOSE_INFO imageobject2
            |   imageobject2
    '''
def p_videoobject2(p):
    '''
        videoobject2 : VIDEODATA
    '''
def p_imageobject2(p):
    '''
        imageobject2 : IMAGENDATA
    '''
def p_informaltable(p):
    """
    informaltable :tableobject
        | tablegroup
    """

def p_tableobject(p):
    '''
    tableobject : OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT tableobject
        | OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
    '''

def p_tablegroup(p):
    '''
    tablegroup : OPEN_TGROUP tgroup CLOSE_TGROUP tablegroup
        | OPEN_TGROUP tgroup CLOSE_TGROUP
    '''

def p_tgroup(p):
    '''
    tgroup : OPEN_THEAD thead CLOSE_THEAD tgroup1
        | tgroup1
    '''

def p_tgroup1(p):
    '''
    tgroup1 : OPEN_TFOOT tfoot CLOSE_TFOOT tgroup2
        | tgroup2
    '''

def p_tgroup2(p):
    '''
    tgroup2 : OPEN_TBODY tbody CLOSE_TBODY
    '''


def p_thead(p):
    '''
    thead : OPEN_ROW row CLOSE_ROW thead
        |OPEN_ROW row CLOSE_ROW
    '''

def p_tfoot(p):
    '''
    tfoot : OPEN_ROW row CLOSE_ROW tfoot
        |OPEN_ROW row CLOSE_ROW
    '''


def p_tbody(p):
    '''
    tbody : OPEN_ROW row CLOSE_ROW tbody
        |OPEN_ROW row CLOSE_ROW
    '''

def p_row(p):
    '''
    row : OPEN_ENTRY entry CLOSE_ENTRY row
        | OPEN_ENTRYTBL entrytbl CLOSE_ENTRYTBL row
        | OPEN_ENTRY entry CLOSE_ENTRY
        | OPEN_ENTRYTBL entrytbl CLOSE_ENTRYTBL
    '''

def p_entrybl(p):
    '''
    entrytbl : OPEN_THEAD thead CLOSE_THEAD entrytbl1
        | entrytbl1
    '''
def p_entrybl1(p):
    '''
    entrybl1 : OPEN_TBODY tbody CLOSE_TBODY
    '''

def p_entry(p):
     '''
        entry : text entry
            | OPEN_ITEMIZEDLIST itemizedList CLOSE_ITEMIZEDLIST entry
            | OPEN_IMPORTANT important CLOSE_IMPORTANT entry
            | OPEN_PARA para CLOSE_PARA entry
            | OPEN_SIMPARA simpara CLOSE_SIMPARAENTRY
            | OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT entry
            | OPEN_COMMENT comment CLOSE_COMMENT entry
            | OPEN_ABSTRACT abstract CLOSE_ABSTRACT entry
            | text
            | OPEN_ITEMIZEDLIST itemizedList CLOSE_ITEMIZEDLIST 
            | OPEN_IMPORTANT important CLOSE_IMPORTANT 
            | OPEN_PARA para CLOSE_PARA 
            | OPEN_SIMPARA simpara CLOSE_SIMPARA
            | OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            | OPEN_COMMENT comment CLOSE_COMMENT
            | OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
    '''

def p_itemzedlist(p):
    '''
    itemizedlist : OPEN_LISTITEM listitem CLOSE_LISTITEM itemizedlist
        |  OPEN_LISTITEM listitem CLOSE_LISTITEM
    '''

def p_listitem(p):
    '''
    listitem :  OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST listitem
        |   OPEN_IMPORTANT important CLOSE_IMPORTANT listitem
        |   OPEN_PARA para CLOSE_PARA listitem
        |   OPEN_SIMPARA simpara CLOSE_SIMPARA listitem
        |   OPEN_ADDRESS address CLOSE_ADDRESS listitem
        |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT listitem
        |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE listitem
        |   OPEN_COMMENT comment CLOSE_COMMENT listitem
        |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT listitem  
        |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST
        |   OPEN_IMPORTANT important CLOSE_IMPORTANT 
        |   OPEN_PARA para CLOSE_PARA
        |   OPEN_SIMPARA simpara CLOSE_SIMPARA
        |   OPEN_ADDRESS address CLOSE_ADDRESS 
        |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
        |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE 
        |   OPEN_COMMENT comment CLOSE_COMMENT 
        |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
    '''
def p_text(p):
    '''
        text : TEXT
    '''

# Manejo de errores
def p_error(p):
    if p:
        print("Error de sintaxis en el token '%s'" % p.value)
    else:
        print("Error de sintaxis en la entrada")

#Ejecutar parser, CORREGIR

ctrl = input("Presione (1) para ingresar la dirección del archivo txt o (2) para ingresar por teclado: ")
if ctrl == "1":
    direccion = input("Ingrese la dirección del archivo txt: ")
    file = open(direccion, "r")
    data = file.read()
    print("Se cargó el archivo:", data)
elif ctrl == "2":
    data = input("Ingrese la cadena que desea comprobar: ")
    print("La cadena escrita es:", data)

lexer = lex.lexer()
lexer.input(data)
error = False

while True:
    tok = lexer.token()
    print(tok)
    if tok is None:
        break
    elif tok.value == "true":
        error = True

if error:
    print("El lenguaje tiene un error en...")  # Debes especificar en qué parte hay un error
else:
    print("¡Lenguaje escrito correctamente!")

parser = yacc.yacc()
result = parser.parse(data)

 """
/Formato DockType
            with open("archivo.html","a") as file:
                file.write("<!DOCKTYPE html>\n".format(text))
        
        //Formato Title Principal
             with open("archivo.html","a") as file:
                file.write("<H1></H1>\n".format(text))
        
        //Formato Titulo en Secciones 
             with open("archivo.html","a") as file:
                file.write("<H2></H2>\n".format(text))
        
        //Formato adentro de Info
            
        
        //Formato adentro etiqueta Important
        
        //Transformacion Etiqueta Para o SimPara
             with open("archivo.html","a") as file:
                file.write("<p></p>\n".format(text))
        
        //Transformacion Etiqueta Link
             with open("archivo.html","a") as file:
                file.write("<></>\n".format(text))
        
        //Transformación Tabla
            //transformacion thead
                with open("archivo.html","a") as file:
                file.write("<th></th>\n".format(text))
            
            //transformacion tfoot
                with open("archivo.html","a") as file:
                file.write("<td></td>\n".format(text))
            //transformacion tbody
                with open("archivo.html","a") as file:
                file.write("<tr></tr>\n".format(text))
        
        //Transformación Itemized List
             with open("archivo.html","a") as file:
                file.write("<ul></ul>\n".format(text))
         //Transformación List Item
             with open("archivo.html","a") as file:
                file.write("<ul></ul>\n".format(text))
 """
        
                
