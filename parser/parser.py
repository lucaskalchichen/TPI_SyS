import ply.yacc as yacc
from calclex import tokens

def p_article(p):
  'article : OPEN_INFO CLOSE_INFO article1'           #algo asi sería(?
  p[0] = <info></info> p[1]
