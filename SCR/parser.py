import tkinter as tk

from tkinter import filedialog

from lexer import archivo_html,tokens

import ply.yacc as yacc



# reglas Gramaticales

def p_start(p):
    '''
    start : document
    '''
    

def p_document(p):
    '''
    document : DOCTYPE_ARTICLE OPEN_ARTICLE article CLOSE_ARTICLE
    '''


def p_article(p):
    '''
        article : OPEN_INFO info CLOSE_INFO article1
            |   article1
    '''
    
    
def p_article1(p):
    '''
        article1 :  open_titlearticle OPEN_TITLE title  close_titlearticle CLOSE_TITLE article2
            | article2
    '''


def p_open_titlearticle(p):
    "open_titlearticle :"
    archivo_html.write('<h1>')


def p_close_titlearticle(p):
    " close_titlearticle : "
    archivo_html.write('</h1>')


def p_article2(p):
    '''
        article2 : article2 OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST 
            |   article2 OPEN_IMPORTANT important CLOSE_IMPORTANT 
            |   article2 OPEN_PARA para CLOSE_PARA 
            |   article2 OPEN_SIMPARA simpara CLOSE_SIMPARA 
            |   article2 OPEN_ADDRESS address CLOSE_ADDRESS 
            |   article2 OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            |   article2 OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE 
            |   article2 OPEN_COMMENT comment CLOSE_COMMENT 
            |   article2 OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDRESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST article3section
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT article3section
            |   OPEN_PARA para CLOSE_PARA article3section
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA article3section
            |   OPEN_ADDRESS address CLOSE_ADDRESS article3section
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT article3section
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE article3section
            |   OPEN_COMMENT comment CLOSE_COMMENT article3section
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT article3section
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST article3simsection
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT article3simsection
            |   OPEN_PARA para CLOSE_PARA article3simsection
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA article3simsection
            |   OPEN_ADDRESS address CLOSE_ADDRESS article3simsection
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT article3simsection
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE article3simsection
            |   OPEN_COMMENT comment CLOSE_COMMENT article3simsection
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT article3simsection
    '''
    

def p_article3section(p):
    '''
        article3section :  article3section OPEN_SECTION section CLOSE_SECTION 
            |   OPEN_SECTION section CLOSE_SECTION
    '''
    

def p_article3simsection(p):
    '''
    article3simsection  : article3simsection OPEN_SIMPLESEC simplesec CLOSE_SIMPLESEC 
        | OPEN_SIMPLESEC simplesec CLOSE_SIMPLESEC
    '''
    

def p_section(p):
    '''
        section : OPEN_INFO info CLOSE_INFO section1
            |   section1
    '''


def p_section1(p):
    '''
        section1 :  open_titleSS  OPEN_TITLE title close_titleSS CLOSE_TITLE section2
            |   section2
    '''


def p_open_titleSS(p):
    "open_titleSS : "
    archivo_html.write('<h2>')


def p_close_titleSS(p):
    "close_titleSS : "
    archivo_html.write('</h2>')    


def p_section2(p):
    '''
        section2 : section2 OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST 
            |   section2 OPEN_IMPORTANT important CLOSE_IMPORTANT 
            |   section2 OPEN_PARA para CLOSE_PARA 
            |   section2 OPEN_SIMPARA simpara CLOSE_SIMPARA 
            |   section2 OPEN_ADDRESS address CLOSE_ADDRESS 
            |   section2 OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            |   section2 OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE 
            |   section2 OPEN_COMMENT comment CLOSE_COMMENT 
            |   section2 OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT
            |   OPEN_PARA para CLOSE_PARA
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA
            |   OPEN_ADDRESS address CLOSE_ADDRESS
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST section3section
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT section3section
            |   OPEN_PARA para CLOSE_PARA section3section
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA section3section
            |   OPEN_ADDRESS address CLOSE_ADDRESS section3section
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT section3section
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE section3section
            |   OPEN_COMMENT comment CLOSE_COMMENT section3section
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT section3section
            |   OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST section3simsection
            |   OPEN_IMPORTANT important CLOSE_IMPORTANT section3simsection
            |   OPEN_PARA para CLOSE_PARA section3simsection
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA section3simsection
            |   OPEN_ADDRESS address CLOSE_ADDRESS section3simsection
            |   OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT section3simsection
            |   OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE section3simsection
            |   OPEN_COMMENT comment CLOSE_COMMENT section3simsection
            |   OPEN_ABSTRACT abstract CLOSE_ABSTRACT section3simsection
    '''
  
        
def p_section3section(p):
    '''
    section3section : section3section OPEN_SECTION section CLOSE_SECTION 
        |   OPEN_SECTION section CLOSE_SECTION
    '''


def p_section3simsection(p):
    '''
    section3simsection  : section3simsection OPEN_SIMPLESEC simplesec CLOSE_SIMPLESEC 
        | OPEN_SIMPLESEC simplesec CLOSE_SIMPLESEC
    '''
    

def p_simplesec(p):
    '''
        simplesec : OPEN_INFO info CLOSE_INFO simplesec1
            |   simplesec1
    '''
    

def p_simplesec1(p):
    '''
        simplesec1 :  open_titleSS title close_titleSS simplesec2
            |   simplesec2
    '''
    

def p_simplesec2(p):
    '''
        simplesec2 : simplesec2 OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST 
            |   simplesec2 OPEN_IMPORTANT important CLOSE_IMPORTANT 
            |   simplesec2 OPEN_PARA  para CLOSE_PARA 
            |   simplesec2 OPEN_SIMPARA simpara CLOSE_SIMPARA 
            |   simplesec2 OPEN_ADDRESS address CLOSE_ADDRESS 
            |   simplesec2 OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            |   simplesec2 OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE 
            |   simplesec2 OPEN_COMMENT comment CLOSE_COMMENT 
            |   simplesec2 OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
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
    

def p_info(p):
    '''
        info : info OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            |   info OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
            |   info OPEN_ADDRESS address CLOSE_ADDRESS 
            |   info OPEN_AUTHOR author CLOSE_AUTHOR 
            |   info OPEN_DATE date CLOSE_DATE 
            |   info OPEN_COPYRIGHT copyright CLOSE_COPYRIGHT 
            |   info OPEN_TITLE title CLOSE_TITLE 
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
        abstract2 : abstract2 OPEN_PARA para CLOSE_PARA 
            |   abstract2 OPEN_SIMPARA simpara CLOSE_SIMPARA abstract2 
            |   OPEN_PARA para CLOSE_PARA abstract2 
            |   OPEN_SIMPARA simpara CLOSE_SIMPARA 
    '''
    

def p_author(p):
    '''
        author : author OPEN_FIRSTNAME firstname CLOSE_FIRSTNAME 
            |   author OPEN_SURNAME surname CLOSE_SURNAME 
            |   OPEN_FIRSTNAME firstname CLOSE_FIRSTNAME 
            |   OPEN_SURNAME simpara CLOSE_SURNAME
    '''
    
def p_address(p):
    '''
        address : address text 
            |   address OPEN_STREET street CLOSE_STREET 
            |   address OPEN_CITY city CLOSE_CITY 
            |   address OPEN_STATE state CLOSE_STATE 
            |   address OPEN_PHONE phone CLOSE_PHONE 
            |   address OPEN_EMAIL email CLOSE_EMAIL 
            |   text 
            |   OPEN_STREET street CLOSE_STREET 
            |   OPEN_CITY city CLOSE_CITY 
            |   OPEN_STATE state CLOSE_STATE 
            |   OPEN_PHONE phone CLOSE_PHONE 
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   empty
    '''
    

def p_empty(p):
    'empty :'
    pass

def p_copyright(p):
    '''
        copyright : OPEN_YEAR year CLOSE_YEAR 
            |    copyright OPEN_YEAR year CLOSE_YEAR  
            |   OPEN_YEAR year CLOSE_YEAR copyright2
    '''
    

def p_copyright2(p):
    '''
        copyright2 : OPEN_HOLDER holder CLOSE_HOLDER 
            |   copyright2 OPEN_HOLDER holder CLOSE_HOLDER 
    '''
    

def p_title(p):
   '''
        title : title text 
            |   title OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   title OPEN_LINK link CLOSE_LINK 
            |   title OPEN_EMAIL email CLOSE_EMAIL 
            |   text 
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMAIL email CLOSE_EMAIL
    '''
   print('Paso tittle')
   

def p_simpara(p):
    '''
    simpara : simpara text 
            |   simpara OPEN_LINK link CLOSE_LINK 
            |   simpara OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   simpara OPEN_EMAIL email CLOSE_EMAIL 
            |   simpara OPEN_AUTHOR author CLOSE_AUTHOR  
            |   simpara OPEN_COMMENT comment CLOSE_COMMENT 
            |   text 
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   OPEN_AUTHOR author CLOSE_AUTHOR  
    '''
    print('Paso simpara')


def p_link(p):
    '''
    link : link text 
            |   link OPEN_LINK link CLOSE_LINK
            |   link OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   link OPEN_EMAIL email CLOSE_EMAIL
            |   link OPEN_AUTHOR author CLOSE_AUTHOR 
            |   link OPEN_COMMENT comment CLOSE_COMMENT
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   OPEN_AUTHOR author CLOSE_AUTHOR  
    '''
    print('Paso link')

def p_emphasis(p):
    '''
    emphasis : emphasis text 
            |   emphasis OPEN_LINK link CLOSE_LINK 
            |   emphasis OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   emphasis OPEN_EMAIL email CLOSE_EMAIL 
            |   emphasis OPEN_AUTHOR author CLOSE_AUTHOR  
            |   emphasis OPEN_COMMENT comment CLOSE_COMMENT 
            |   text 
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   OPEN_AUTHOR author CLOSE_AUTHOR  
    '''
    print('Paso emphasis')

def p_comment(p):
    '''
    comment : comment text 
            |   comment OPEN_LINK link CLOSE_LINK 
            |   comment OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   comment OPEN_EMAIL email CLOSE_EMAIL 
            |   comment OPEN_AUTHOR author CLOSE_AUTHOR  
            |   comment OPEN_COMMENT comment CLOSE_COMMENT 
            |   text 
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
            |   OPEN_EMAIL email CLOSE_EMAIL 
            |   OPEN_AUTHOR author CLOSE_AUTHOR  
    '''


def p_para(p):
    '''
            para : para text 
            |   para OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   para OPEN_LINK link CLOSE_LINK 
            |   para OPEN_EMAIL email CLOSE_EMAIL 
            |   para OPEN_AUTHOR author CLOSE_AUTHOR 
            |   para OPEN_COMMENT comment CLOSE_COMMENT 
            |   para OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST 
            |   para OPEN_IMPORTANT important CLOSE_IMPORTANT 
            |   para OPEN_ADDRESS address CLOSE_ADDRESS 
            |   para OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            |   para OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE 
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
        important2 : important2 OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST 
            |   important2 OPEN_IMPORTANT important CLOSE_IMPORTANT 
            |   important2 OPEN_PARA para CLOSE_PARA 
            |   important2 OPEN_SIMPARA simpara CLOSE_SIMPARA 
            |   important2 OPEN_ADDRESS address CLOSE_ADDRESS 
            |   important2 OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            |   important2 OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE 
            |   important2 OPEN_COMMENT comment CLOSE_COMMENT 
            |   important2 OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
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
    #esto anda
    

def p_firstname(p):
    '''
        firstname : firstname text
            |   firstname OPEN_LINK link CLOSE_LINK
            |   firstname OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   firstname OPEN_COMMENT comment CLOSE_COMMENT
            |   text 
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''


def p_surname(p):
    '''
        surname : surname text 
            |   surname OPEN_LINK link CLOSE_LINK 
            |   surname OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   surname OPEN_COMMENT comment CLOSE_COMMENT 
            |   text 
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''


def p_street(p):
    '''
        street : street text 
            |   street OPEN_LINK link CLOSE_LINK 
            |   street OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   street OPEN_COMMENT comment CLOSE_COMMENT 
            |   text 
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
    

def p_city(p):
    '''
        city : city text 
            |   city OPEN_LINK link CLOSE_LINK 
            |   city OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   city OPEN_COMMENT comment CLOSE_COMMENT 
            |   text 
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
    


def p_state(p):
    '''
        state : state text 
            |   state OPEN_LINK link CLOSE_LINK 
            |   state OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   state OPEN_COMMENT comment CLOSE_COMMENT 
            |   text 
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
    


def p_phone(p):
    '''
        phone : phone text 
            |   phone OPEN_LINK link CLOSE_LINK 
            |   phone OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   phone OPEN_COMMENT comment CLOSE_COMMENT 
            |   text 
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
    


def p_email(p):
    '''
        email : email text
            |   email OPEN_LINK link CLOSE_LINK
            |   email OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   email OPEN_COMMENT comment CLOSE_COMMENT
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
    


def p_date(p):
    '''
        date : date text 
            |   date OPEN_LINK link CLOSE_LINK 
            |   date OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   date OPEN_COMMENT comment CLOSE_COMMENT 
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
    


def p_year(p):
    '''
        year : year text 
            |   year OPEN_LINK link CLOSE_LINK 
            |   year OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   year OPEN_COMMENT comment CLOSE_COMMENT 
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
    


def p_holder(p):
    '''
        holder : holder text 
            |   holder OPEN_LINK link CLOSE_LINK 
            |   holder OPEN_EMPHASIS emphasis CLOSE_EMPHASIS 
            |   holder OPEN_COMMENT comment CLOSE_COMMENT 
            |   text
            |   OPEN_LINK link CLOSE_LINK
            |   OPEN_EMPHASIS emphasis CLOSE_EMPHASIS
            |   OPEN_COMMENT comment CLOSE_COMMENT
    '''
    


def p_mediaobject(p):
    '''
        mediaobject : OPEN_INFO info CLOSE_INFO mediadata
            |   mediadata
    '''
    


def p_mediadata(p):
    '''
        mediadata : OPEN_VIDEOOBJECT videoobject CLOSE_VIDEOOBJECT mediadata2
            |  OPEN_IMAGENOBJECT imageobject CLOSE_IMAGENOBJECT mediadata2
            |  OPEN_VIDEOOBJECT videoobject CLOSE_VIDEOOBJECT
            |  OPEN_IMAGENOBJECT imageobject CLOSE_IMAGENOBJECT
    '''
    


def p_mediadata2(p):
    '''
        mediadata2 : OPEN_VIDEOOBJECT videoobject CLOSE_VIDEOOBJECT 
            |   OPEN_IMAGENOBJECT imageobject CLOSE_IMAGENOBJECT 
            |  mediadata2 OPEN_VIDEOOBJECT videoobject CLOSE_VIDEOOBJECT
            |  mediadata2 OPEN_IMAGENOBJECT imageobject CLOSE_IMAGENOBJECT
    '''
    

def p_videoobject(p):
    '''
        videoobject : videoobject2 OPEN_INFO info CLOSE_INFO 
            |   videoobject2
    '''
    


def p_imageobject(p):
    '''
        imageobject :  OPEN_INFO info CLOSE_INFO imageobject2
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
    informaltable : tableobject
        | tablegroup
    """
    


def p_tableobject(p):
    '''
    tableobject : OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
        | tableobject OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
    '''
    



def p_tablegroup(p):
    '''
    tablegroup : OPEN_TGROUP tgroup CLOSE_TGROUP 
        | tablegroup OPEN_TGROUP tgroup CLOSE_TGROUP
    '''
    


def p_tgroup(p):
    '''
    tgroup :  OPEN_THEAD thead CLOSE_THEAD tgroup1
        | tgroup1
    '''
    


def p_tgroup1(p):
    '''
    tgroup1 :  OPEN_TFOOT tfoot CLOSE_TFOOT tgroup2
        | tgroup2
    '''
    


def p_tgroup2(p):
    '''
    tgroup2 : OPEN_TBODY tbody CLOSE_TBODY
    '''
    



def p_thead(p):
    '''
    thead : OPEN_ROW row CLOSE_ROW 
        |   thead OPEN_ROW row CLOSE_ROW
    '''
    


def p_tfoot(p):
    '''
    tfoot : OPEN_ROW row CLOSE_ROW 
        |   tfoot OPEN_ROW row CLOSE_ROW
    '''
    


def p_tbody(p):
    '''
    tbody : OPEN_ROW row CLOSE_ROW 
        |   tbody OPEN_ROW row CLOSE_ROW
    '''
    


def p_row(p):
    '''
    row : OPEN_ENTRY entry CLOSE_ENTRY 
        | OPEN_ENTRYTBL entrytbl CLOSE_ENTRYTBL 
        | row OPEN_ENTRY entry CLOSE_ENTRY
        | row OPEN_ENTRYTBL entrytbl CLOSE_ENTRYTBL
    '''
    

def p_entrytbl(p):
    '''
    entrytbl :  OPEN_THEAD thead CLOSE_THEAD entrytbl1
        | entrytbl1
    '''
    


def p_entrytbl1(p):
    '''
    entrytbl1 : OPEN_TBODY tbody CLOSE_TBODY
    '''
    

def p_entry(p):
    '''
        entry : entry text 
            | entry OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST 
            | entry OPEN_IMPORTANT important CLOSE_IMPORTANT 
            | entry OPEN_PARA para CLOSE_PARA 
            | entry OPEN_SIMPARA simpara CLOSE_SIMPARA 
            | entry OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
            | entry OPEN_COMMENT comment CLOSE_COMMENT 
            | entry OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
            | text 
            | OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST 
            | OPEN_IMPORTANT important CLOSE_IMPORTANT 
            | OPEN_PARA para CLOSE_PARA 
            | OPEN_SIMPARA simpara CLOSE_SIMPARA
            | OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT
            | OPEN_COMMENT comment CLOSE_COMMENT
            | OPEN_ABSTRACT abstract CLOSE_ABSTRACT 
    '''

    #esto anda
    

def p_itemzedlist(p):
    '''
    itemizedlist : OPEN_LISTITEM listitem CLOSE_LISTITEM 
        |  itemizedlist OPEN_LISTITEM listitem CLOSE_LISTITEM
    '''
    


def p_listitem(p):
    '''
    listitem :  listitem OPEN_ITEMIZEDLIST itemizedlist CLOSE_ITEMIZEDLIST 
        |   listitem OPEN_IMPORTANT important CLOSE_IMPORTANT 
        |   listitem OPEN_PARA para CLOSE_PARA 
        |   listitem OPEN_SIMPARA simpara CLOSE_SIMPARA 
        |   listitem OPEN_ADDRESS address CLOSE_ADDRESS 
        |   listitem OPEN_MEDIAOBJECT mediaobject CLOSE_MEDIAOBJECT 
        |   listitem OPEN_INFORMALTABLE informaltable CLOSE_INFORMALTABLE 
        |   listitem OPEN_COMMENT comment CLOSE_COMMENT 
        |   listitem OPEN_ABSTRACT abstract CLOSE_ABSTRACT   
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
    #esto anda




    
def p_text(p):
    '''
        text : TEXT
    '''
   


#ERRORES
def p_error(p):
    if p:
        print("Error de sintaxis en el token '%s'" % p.value)
    else:
        print("Error de sintaxis en la entrada")

#EJECUTAR EL ARCHIVO




def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    etiqueta = tk.Label(ventana, text="Archivo seleccionado: " + archivo)
    etiqueta.pack()
    def ejecutar_parser():
        with open(archivo, 'r') as file:
            data = file.read()

        parser = yacc.yacc()
        parser.parse(data)

        archivo_html.close()


    boton_ejecutar = tk.Button(ventana, text="Ejecutar", state=tk.NORMAL, command=ejecutar_parser)
    boton_ejecutar.pack()

def mostrar_ventana_entrada():
    def ejecutar_parser():
        data = entrada_texto.get()

        parser = yacc.yacc()
        parser.parse(data)
         
        archivo_html.close()
        

    ventana_entrada = tk.Toplevel(ventana)
    ventana_entrada.title("Ventana de Entrada")
    ventana_entrada.geometry("800x400")
    
    etiqueta_entrada = tk.Label(ventana_entrada, text="Ingrese un texto")
    etiqueta_entrada.pack()
    
    entrada_texto = tk.Entry(ventana_entrada)
    entrada_texto.pack()

    boton_ejecutar = tk.Button(ventana_entrada, text="Ejecutar", state=tk.NORMAL, command=ejecutar_parser)
    boton_ejecutar.pack()
    
    boton_salir_entrada = tk.Button(ventana_entrada, text="Salir", command=ventana_entrada.destroy)
    boton_salir_entrada.pack()

def cerrar_interfaz(event):
    if event.keysym == 'd' and event.state == 4:  # Comprueba si se presionó Control + D
        ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador Sintactico DOCBOOK")
ventana.geometry("800x400")

# Crear los elementos de la interfaz
etiqueta = tk.Label(ventana, text="Presiona el botón 'Archivo de Lectura' para seleccionar un archivo de lectura del parser.\nPresiona el botón 'Modo Interactivo' para ingresar el texto del deseas realizar la comprobacion sintatica.")
etiqueta.pack()

boton1 = tk.Button(ventana, text="Archivo de Lectura", command=abrir_archivo)
boton1.pack()

boton2 = tk.Button(ventana, text="Modo Interactivo", command=mostrar_ventana_entrada)
boton2.pack()

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack()

# Vincular el cierre de la interfaz a la combinación de teclas Control + D
ventana.bind('<Control-d>', cerrar_interfaz)

# Iniciar el bucle principal de la ventana
ventana.mainloop()




"""
/Formato DockType
            with open("archivo.html","a") as file:
                file.write("<!DOCKTYPE html>\n")
        
        //Formato Title Principal
             with open("archivo.html","a") as file:
                file.write("<H1></H1>\n")
        
        //Formato Titulo en Secciones 
             with open("archivo.html","a") as file:
                file.write("<H2></H2>\n")
        
        //Formato adentro de Info
            
        
        //Formato adentro etiqueta Important
        
        //Transformacion Etiqueta Para o SimPara
             with open("archivo.html","a") as file:
                file.write("<p></p>\n")
        
        //Transformacion Etiqueta Link
             with open("archivo.html","a") as file:
                file.write("<></>\n")
        
        //Transformación Tabla
            //transformacion thead
                with open("archivo.html","a") as file:
                file.write("<th></th>\n")
            
            //transformacion tfoot
                with open("archivo.html","a") as file:
                file.write("<td></td>\n")
            //transformacion tbody
                with open("archivo.html","a") as file:
                file.write("<tr></tr>\n")
        
        //Transformación Itemized List
             with open("archivo.html","a") as file:
                file.write("<ul></ul>\n")
         //Transformación List Item
             with open("archivo.html","a") as file:
                file.write("<ul></ul>\n")
 """

        
                
