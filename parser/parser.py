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
            |   aticle1
    '''

def p_article1(p):
    '''
        article1 :  OPEN_TITLE title ClOSE_TITLE article2
        article1 :  article2
    '''
def p_article2(p):
    '''
        article2 : OPEN_LISTITEM itemlist CLOSE_LISTITEM article2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT article2
            |   OPEN_PARA  para CLOSE_PARA article2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA article2
            |   OPEN_ADDREESS address CLOSE_ADDRESS article2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT article2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE article2
            |   OPEN_COMMENT comment CLOSE_COMMENT article2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT article2
            |   OPEN_LISTITEM itemlist CLOSE_LISTITEM
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDREESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
            |   OPEN_LISTITEM itemlist CLOSE_LISTITEM article3
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT article3
            |   OPEN_PARA para CLOSE_PARA article3
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA article3
            |   OPEN_ADDREESS address CLOSE_ADDRESS article3
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT article3
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE article3
            |   OPEN_COMMENT comment CLOSE_COMMENT article3
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT article3
    '''

def p_article3(p):
    '''
        article3 :  OPEN_SIMSECT simsect CLOUSE_SIMPLESECT 
        |   OPEN_SECTION section CLOUSE_SECTION

        | OPEN_SIMSECT CLOUSE_SIMPLESECT article3simsect
        | OPEN_SECTION section CLOUSE_SECTION article3section
    
    '''
def p_article3section(p):
    '''
    article3section:    OPEN_SECTION section CLOUSE_SECTION article3section
    | OPEN_SECTION  section CLOUSE_SECTION
    '''
def p_article3(p):
    '''
    article3simsect : OPEN_SIMSECT simsect CLOUSE_SIMPLESECT article3simsect
        |   OPEN_SIMSECT simsect CLOUSE_SIMPLESECT 
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
        section2 : OPEN_LISTITEM itemlist CLOSE_LISTITEM section2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT section2
            |   OPEN_PARA  para CLOSE_PARA section2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA section2
            |   OPEN_ADDREESS address CLOSE_ADDRESS section2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT section2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE section2
            |   OPEN_COMMENT comment CLOSE_COMMENT section2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT section2
            |   OPEN_LISTITEM itemlist CLOSE_LISTITEM
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDREESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
            |   OPEN_LISTITEM itemlist CLOSE_LISTITEM section3
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT section3
            |   OPEN_PARA para CLOSE_PARA section3
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA section3
            |   OPEN_ADDREESS address CLOSE_ADDRESS section3
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT section3
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE section3
            |   OPEN_COMMENT comment CLOSE_COMMENT section3
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT section3
    '''

def p_section3(p):
    '''
    section3 :  OPEN_SIMSECT simsect CLOUSE_SIMPLESECT
        |   OPEN_SECTION section CLOUSE_SECTION

        | OPEN_SIMSECT CLOUSE_SIMPLESECT section3simsect
        | OPEN_SECTION section CLOUSE_SECTION section3section
    '''

def p_section3section(p):
    '''
    section3section:    OPEN_SECTION section CLOUSE_SECTION section3section
    | OPEN_SECTION  section CLOUSE_SECTION
    '''

def p_section3simsect(p):
    '''
    section3simsect : OPEN_SIMSECT simsect CLOUSE_SIMPLESECT section3simsect
        |   OPEN_SIMSECT simsect CLOUSE_SIMPLESECT
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
        simplesec2 : OPEN_LISTITEM itemlist CLOSE_LISTITEM simplesec2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT simplesec2
            |   OPEN_PARA  para CLOSE_PARA simplesec2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA simplesec2
            |   OPEN_ADDREESS address CLOSE_ADDRESS simplesec2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT simplesec2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE simplesec2
            |   OPEN_COMMENT comment CLOSE_COMMENT simplesec2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT simplesec2
            |   OPEN_LISTITEM itemlist CLOSE_LISTITEM
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDREESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
    '''

def p_info(p):
     '''
        info : OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT info
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT info
            |   OPEN_ADDREESS address CLOSE_ADDREESS info
            |   OPEN_AUTHOR author CLOSE_AUTHOR info
            |   OPEN_DATE date CLOSE_DATE info
            |   OPEN_COPYRIGHT copyright CLOSE_COPYRIGHT info
            |   OPEN_TITLE title CLOSE_TITLE info
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
            |   OPEN_ADDREESS address CLOSE_ADDREESS 
            |   OPEN_AUTHOR author CLOSE_AUTHOR 
            |   OPEN_DATE date CLOSE_DATE 
            |   OPEN_COPYRIGHT copyright CLOSE_COPYRIGHT 
            |   OPEN_TITLE title CLOSE_TITLE
    '''

def p_abstract(p):
    '''
        abstract : OPEN_TITLE title CLOSE_TITLE abstract
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
            |   empy
    '''

def p_empt(p):
    pass

def p_copyright(p):
    '''
        copyright : OPEN_YEAR year CLOSE_YEAR copyright2 
            |   OPEN_YEAR year CLOSE_YEAR
    '''

def p_copyright2(p):
     '''
        copyright2 : OPEN_YEAR year CLOSE_YEAR copyright2
            |   copyright3
    '''

def p_copyright3(p):
     '''
        copyright3 : OPEN_HOLDER holder CLOSE_HOLDER copyright3
            |   OPEN_HOLDER holder CLOSE_HOLDER
    '''
def p_title(p):
   '''
        title : text title
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS title
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMAIL email CLOSE_EMAIL title
            |   text
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMAIL email CLOSE_EMAIL
    '''



def p_important(p):
     '''
        important : OPEN_TITLE title CLOSE_TITLE important2
            |   important2

    '''

def p_important2(p):
     '''
        important2 : OPEN_LISTITEM itemlist CLOSE_LISTITEM important2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT important2
            |   OPEN_PARA para CLOSE_PARA important2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA important2
            |   OPEN_ADDRESS address CLOSE_ADDRESS important2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT important2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE important2
            |   OPEN_COMMENT comment CLOSE_COMMENT important2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT important2
            |   OPEN_LISTITEM itemlist CLOSE_LISTITEM
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDRESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT

    '''
def p_firstname(p):
    '''
        firstname : text firstname
            |   OPEN_LINK link CLOSE_LINK firstname
            |   OPEN_EMPHASIS enphasis CLOSE_EMPHASIS firstname
            |   OPEN_COMMENT comment CLOSE_COMMENT firstname
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_surname(p):
    '''
        surname : text surname
            |   OPEN_LINK link CLOSE_LINK surname
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS surname
            |   OPEN_COMMENT comment CLOSE_COMMENT surname
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_street(p):
     '''
        street : text street
            |   OPEN_LINK link CLOSE_LINK street
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS street
            |   OPEN_COMMENT comment CLOSE_COMMENT street
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_city(p):
    '''
        city : text city
            |   OPEN_LINK link CLOSE_LINK city
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS city
            |   OPEN_COMMENT comment CLOSE_COMMENT city
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_state(p):
    '''
        state : text state
            |   OPEN_LINK link CLOSE_LINK state
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS state
            |   OPEN_COMMENT comment CLOSE_COMMENT state
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_phone(p):
     '''
        phone : text phone
            |   OPEN_LINK link CLOSE_LINK phone
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS phone
            |   OPEN_COMMENT comment CLOSE_COMMENT phone
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_email(p):
    '''
        email : text email
            |   OPEN_LINK link CLOSE_LINK email
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS email
            |   OPEN_COMMENT comment CLOSE_COMMENT email
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_date(p):
    '''
        date : text date
            |   OPEN_LINK link CLOSE_LINK date
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS date
            |   OPEN_COMMENT comment CLOSE_COMMENT date
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_year(p):
     '''
        year : text year
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS year
            |   OPEN_COMMENT comment CLOSE_COMMENT year
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_holder(p):
    '''
        holder : text holder
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS holder
            |   OPEN_COMMENT comment CLOSE_COMMENT holder
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
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

def para(p):
    '''
            para : text para
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS para
            |   OPEN_LINK link CLOSE_LINK para
            |   OPEN_EMAIL email CLOSE_EMAIL para
            |   OPEN_AUTHOR author CLOSE_AUTHOR para
            |   OPEN_COMMENT comment CLOSE_COMMENT para
            |   OPEN_LISTITEM listitem CLOSE_LISTITEM para
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
            |   OPEN_LISTITEM listitem CLOSE_LISTITEM
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT 
            |   OPEN_ADDRESS address CLOSE_ADDRESS 
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE 
        
    '''


def p_mediaobject(p):
     '''
        mediaobject : OPEN_INFO info CLOSE_INFO mediadata
            |   mediadata
    '''
def p_mediadata(p):
     '''
        mediadata : videoobject mediadata2
            |  imageobject mediadata3
    '''
def p_mediadata2(p):
     '''
        mediadata2 : videoobject mediadata2
            |   imageobject mediadata2
    '''
def p_mediadata3(p):
     '''
        mediadata3 : videoobject mediadata3
            |   imageobject mediadata3
    '''
def p_videoobject(p):
    '''
        videoobject : OPEN_INFO TEXT CLOSE_INFO videoobject2
            |   videoobject2
    '''
def p_imageobject(p):
    '''
        imageobject : OPEN_INFO TEXT CLOSE_INFO imageobject2
            |   imageobject2
    '''
def p_videoobject2(p):
    '''
        videoobject2 : OPEN_VIDEOOBJECT VIDEODATA CLOSE_VIDEOOBJECT
    '''
def p_imageobject2(p):
    '''
        imageobject2 : OPEN_IMAGENOBJECT IMAGENDATA CLOSE_IMAGENLOBJECT
    '''

def p_informaltable(p):
    """
    informaltable :tableobject
        | tablegroup
    """

def p_tableobject(p):
    '''
    tableobject : mediaobject tableobject
        | mediaobject
    '''

def p_tablegroup(p):
    '''
    tablegroup : tgroup tablegroup
        | tgroup
    '''

def p_tgroup(p):
    '''
    tgroup : thead tgroup1
        | tgroup1
    '''

def p_tgroup1(p):
    '''
    tgroup1 : tgroup2
    '''

def p_tgroup2(p):
    '''
    tgroup2 : tfoot tgroup3
    | tgroup3
    '''

def p_tgroup3(p):
    '''
    tgroup3 : tbody
    '''

def p_thead(p):
    '''
    thead : bloque
    '''

def p_tfoot(p):
    '''
    tfoot : bloque
    '''


def p_tbody(p):
    '''
    tbody : bloque
    '''

def p_bloque(p):
    '''
    bloque :row bloque
        |row
    '''

def p_row(p):
    '''
    row : entry row
        | entrytbl row
        | entry
        | entrytbl
    '''

def p_entrybl1(p):
    '''
    entrytbl : thead entrytbl1
        | entrytbl1
        | tbody
    '''

def p_entry(p):
    """
        entry : text entry
            | CLOSE_ITEMIZEDLIST temizedList  CLOSE_ITEMIZEDLIST entry
            | OPEN_IMPORTANT important CLOSE_IMPORTANT entry
            | OPEN_PARA para CLOSE_PARA entry
            | OPEN_SIMPARA simpara CLOSE_SIMPARAENTRY
            | OPEN_MEDIAOBJECT comment CLOSE_COMMENT entry
            | OPEN_COMMENT comment CLOSE_COMMENTENTRY
            | OPEN_ABSTRACT abstract CLOSE_ABSTRACT entry
            | text
            | CLOSE_ITEMIZEDLIST temizedList CLOSE_ITEMIZEDLIST 
            | OPEN_IMPORTANT important CLOSE_IMPORTANT 
            | OPEN_PARA para CLOSE_PARA 
            | OPEN_SIMPARA simpara CLOSE_SIMPARA
            | OPEN_MEDIAOBJECT mediaobject CLOSE_COMMENT 
            | OPEN_COMMENT comment CLOSE_COMMENT
            | OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
    """

def p_itemzedlist(p):
    '''
    itemzedlist: listitem itemzedlist
        |   listitem 
    '''

def p_listem(p):
    '''
    listitem:   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST listitem
        |   OPEN_IMPORTANT important CLOSE_IMPORTANT listitem
        |   OPEN_PARA para CLOSE_PARAlistitem
        |   OPEN_SIMPARA simpara CLOSE_SIMPARAlistitem
        |   OPEN_ADDRESS address CLOSE_ADDRESS listitem
        |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT listitem
        |   OPEN_INFORMALTABLE informaltalbe CLOSE_INFORMALTABLE listitem
        |   OPEN_COMMENT comment CLOSE_COMMENT listitem
        |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT listitem  
        |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST
        |   OPEN_IMPORTANT important CLOSE_IMPORTANT 
        |   OPEN_PARA para CLOSE_PARA
        |   OPEN_SIMPARA simpara CLOSE_SIMPARA
        |   OPEN_ADDRESS address CLOSE_ADDRESS 
        |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
        |   OPEN_INFORMALTABLE informaltalbe CLOSE_INFORMALTABLE 
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
