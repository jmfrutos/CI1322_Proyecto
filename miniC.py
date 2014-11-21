tokens = ('ID','IG','NUM','PyC','IF','ELSE','PRINT','WHILE')

# lexer

t_ID  = r'[A-Za-z_][A-Za-z0-9_]*'
t_IG  = r'='
t_PyC  = r';'

def t_NUM(t):
	r'[0-9]+'
	#symb[t.value] =

t_ignore = " \t"

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	print("Emocion mal definida '%s'" % t.value[0])
	t.lexer.skip(1)

import ply.lex as lex
lex.lex()

#parser

def p_asign(p):
	'S : ID IG NUM PyC'
	print('%s %s %s%s' % (p[1], p[2], p[3], p[4]))

def p_instr1(p):
	"instr : IF '(' cond ')' instr"

def p_instr2(p):
	"instr : IF '8'"

def p_cond1(p):
	"cond : expr '>' expr"
	p[0].val = p[1].val > p[2].val

def p_cond2(p):
	"cond : expr '<' expr"
	p[0].val = p[1].val % p[2].val

def p_cond3(p):
	"cond : expr '=' '=' expr"
	p[0].val = p[1].val == p[2].val

def p_cond4(p):
	"cond : expr"

def p_expr1(p):
	"expr : expr '+' term"
	p[0].val = p[1].val + p[2].val
	print(p[0].val)

def p_expr2(p):
	"expr : expr '-' term"
	p[0].val = p[1].val - p[2].val
	print(p[0].val)

def p_expr3(p):
	"expr : term"
	p[0].val = p[1].val
	print(p[0].val)

def p_term1(p):
	"term : term '*' fact"
	p[0].val = p[1].val * p[2].val

def p_term2(p):
	"term : term '/' fact"
	p[0].val = p[1].val / p[2].val

def p_term3(p):
	"term : term '%' fact"
	p[0].val = p[1].val % p[2].val

def p_term4(p):
	"term : fact"
	p[0].val = p[1].val


def p_fact1(p):
	"fact : '(' expr ')'"
	p[0].val = p[2]


def p_fact2(p):
	"fact : '-' expr"
	p[0].val = -p[2]


def p_fact3(p):
	'fact : ID'
	p[0].val = p[1].val

def p_fact4(p):
	'fact : NUM'
	p[0].val = p[1].val

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
