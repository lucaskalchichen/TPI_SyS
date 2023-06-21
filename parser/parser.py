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
        article2 : OPEN_LISTITEM itemlits CLOSE_LISTITEM article2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT article2
            |   OPEN_PARA  para CLOSE_PARA article2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA article2
            |   OPEN_ADDREESS address CLOSE_ADDRESS article2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT article2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE article2
            |   OPEN_COMMENT comment CLOSE_COMMENT article2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT article2
            |   OPEN_LISTITEM itemlits CLOSE_LISTITEM
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDREESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
            |   OPEN_LISTITEM itemlits CLOSE_LISTITEM
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
        section2 : OPEN_LISTITEM itemlits CLOSE_LISTITEM section2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT section2
            |   OPEN_PARA  para CLOSE_PARA section2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA section2
            |   OPEN_ADDREESS address CLOSE_ADDRESS section2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT section2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE section2
            |   OPEN_COMMENT comment CLOSE_COMMENT section2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT section2
            |   OPEN_LISTITEM itemlits CLOSE_LISTITEM
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDREESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
            |   OPEN_LISTITEM itemlits CLOSE_LISTITEM
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
        simplesec2 : OPEN_LISTITEM itemlits CLOSE_LISTITEM simplesec2
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT simplesec2
            |   OPEN_PARA  para CLOSE_PARA simplesec2
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA simplesec2
            |   OPEN_ADDREESS address CLOSE_ADDRESS simplesec2
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT simplesec2
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE simplesec2
            |   OPEN_COMMENT comment CLOSE_COMMENT simplesec2
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT simplesec2
            |   OPEN_LISTITEM itemlits CLOSE_LISTITEM
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDREESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
            |   OPEN_LISTITEM itemlits CLOSE_LISTITEM
    '''


def p_title(p):
    '''title : OPEN_TITLE TEXT CLOSE_TITLE'''
    # Acción semántica: Realizar acciones relacionadas con el título

# Otras reglas gramaticales y acciones semánticas...



# Manejo de errores
def p_error(p):
    if p:
        print("Error de sintaxis en el token '%s'" % p.value)
    else:
        print("Error de sintaxis en la entrada")
