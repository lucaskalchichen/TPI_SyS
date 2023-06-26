from lexer.lexer import tokens

import ply.yacc as yacc

# reglas Gramaticales

def p_document(p):
    '''document : doctype article'''
def doctype(p):
    'doctype : DOCTYPE_ARTICLE'  
def p_article(p):
    'article : OPEN_ARTICLE body CLOSE_ARTICLE'
    # Acción semántica: Realizar acciones relacionadas con el artículo

    p[1] ='<article>'
    p[3] ='</article>'
    
    p[0]= p[1] p[2] p[3]
    # Obtener el contenido del body
    article_content = p[2]
    
    # Realizar verificaciones adicionales
    validate_article(article_content)
    
    # Procesar el contenido del artículo
    processed_content = process_article(article_content)
    
    # Generar la salida HTML correspondiente
    html_output = generate_html(processed_content)
    
    # Imprimir la salida HTML
    print(html_output)

def p_body(p):
    '''body : section
    
    
    
    
    '''

def p_section(p):
    '''section : OPEN_SECTION title body CLOSE_SECTION'''
    # Acción semántica: Realizar acciones relacionadas con la sección

def p_sim_section(p);

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

# Manejo de errores
def p_error(p):
    if p:
        print("Error de sintaxis en el token '%s'" % p.value)
    else:
        print("Error de sintaxis en la entrada")
