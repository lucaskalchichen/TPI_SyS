from lexer.lexer import tokens

import ply.yacc as yacc

# reglas Gramaticales

def p_document(p):
    '''document : doctype article'''
    # Acción semántica: Verificar la gramática del documento DocBook
    # Aquí puedes realizar las verificaciones necesarias y manejar los resultados

def doctype(p):
    'doctype : DOCTYPE_ARTICLE'
     # Acción semántica: Verificar la gramática del documento DocBook
    if p[1] != "<!DOCTYPE article>":
        print("Error: El doctype no es válido.")
    else:
        # Realizar acciones relacionadas con el doctype
        doctype_info = extract_doctype_info(p[1])
        process_doctype(doctype_info)

        # Realizar verificaciones y acciones adicionales para el contenido del artículo
        article_content = p[2]
        validate_article_content(article_content)

        # Generar la salida HTML correspondiente
        html_output = generate_html(article_content)
        print(html_output)


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
    # Acción semántica: Realizar acciones relacionadas con el cuerpo del documento

def p_section(p):
    '''section : OPEN_SECTION title body CLOSE_SECTION'''
    # Acción semántica: Realizar acciones relacionadas con la sección

def p_sim_section(p);

def p_title(p):
    '''title : OPEN_TITLE TEXT CLOSE_TITLE'''
    # Acción semántica: Realizar acciones relacionadas con el título

# Otras reglas gramaticales y acciones semánticas...

def p_article(p):
    'article : OPEN_INFO info CLOSE_INFO article'
    p[0] = <info> p[1] </info> p[3]


# Manejo de errores
def p_error(p):
    if p:
        print("Error de sintaxis en el token '%s'" % p.value)
    else:
        print("Error de sintaxis en la entrada")
