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
        title : OPEN_TEXT text CLOSE_TEXT title
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS title
            |   #falta link aca
            |   OPEN_EMAIL email CLOSE_EMAIL title
            |   OPEN_TEXT text CLOSE_TEXT
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   #falta link aca
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
        firstname : OPEN_TEXT text CLOSE_TEXT firstname
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS firstname
            |   OPEN_COMMENT comment CLOSE_COMMENT firstname
            |   OPEN_TEXT text CLOSE_TEXT
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_surname(p):
    '''
        surname : OPEN_TEXT text CLOSE_TEXT surname
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS surname
            |   OPEN_COMMENT comment CLOSE_COMMENT surname
            |   OPEN_TEXT text CLOSE_TEXT
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_street(p):
     '''
        street : OPEN_TEXT text CLOSE_TEXT street
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS street
            |   OPEN_COMMENT comment CLOSE_COMMENT street
            |   OPEN_TEXT text CLOSE_TEXT
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_city(p):
    '''
        city : OPEN_TEXT text CLOSE_TEXT city
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS city
            |   OPEN_COMMENT comment CLOSE_COMMENT city
            |   OPEN_TEXT text CLOSE_TEXT
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_state(p):
    '''
        state : OPEN_TEXT text CLOSE_TEXT state
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS state
            |   OPEN_COMMENT comment CLOSE_COMMENT state
            |   OPEN_TEXT text CLOSE_TEXT
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_phone(p):
     '''
        phone : OPEN_TEXT text CLOSE_TEXT phone
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS phone
            |   OPEN_COMMENT comment CLOSE_COMMENT phone
            |   OPEN_TEXT text CLOSE_TEXT
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_email(p):
    '''
        email : OPEN_TEXT text CLOSE_TEXT email
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS email
            |   OPEN_COMMENT comment CLOSE_COMMENT email
            |   OPEN_TEXT text CLOSE_TEXT
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_date(p):
    '''
        date : OPEN_TEXT text CLOSE_TEXT date
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS date
            |   OPEN_COMMENT comment CLOSE_COMMENT date
            |   OPEN_TEXT text CLOSE_TEXT
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_year(p):
     '''
        year : OPEN_TEXT text CLOSE_TEXT year
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS year
            |   OPEN_COMMENT comment CLOSE_COMMENT year
            |   OPEN_TEXT text CLOSE_TEXT
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
def p_holder(p):
    '''
        holder : OPEN_TEXT text CLOSE_TEXT holder
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS holder
            |   OPEN_COMMENT comment CLOSE_COMMENT holder
            |   OPEN_TEXT text CLOSE_TEXT
            |   #falta link aca
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''

def p_link(p):
    '''
    link : OPEN_LINK XLINK_ATTRIBUTE '=' URL CLOSE_LINK TEXT OPEN_LINK CLOSE_LINK
    '''


# Manejo de errores
def p_error(p):
    if p:
        print("Error de sintaxis en el token '%s'" % p.value)
    else:
        print("Error de sintaxis en la entrada")