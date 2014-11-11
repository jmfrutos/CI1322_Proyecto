tokens = ('ID','IG','NUM','PyC','IF')

# lexer

t_ID  = r'[A-Za-z_][A-Za-z0-9_]*'
t_IG  = r'='
t_NUM  = r'[0-9]+'
t_PyC  = r';'

#def t_VAR(t):
 #   r'[A-Za-z_][A-Za-z0-9_]*'
    #symb[t.value] = 

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Emoción mal definida '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()


#parser

def p_asign(p):
    'S : ID IG NUM PyC'
    print('%s %s %s%s' % (p[1], p[2], p[3], p[4]))
    

def p_error(p):
    if p:
        print("Error de sintaxis en '%s'" % p.value)
    else:
        print("??")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = input('miniC > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)
    

