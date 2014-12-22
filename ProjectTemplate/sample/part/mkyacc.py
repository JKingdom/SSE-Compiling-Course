import mklex
tokens = mklex.tokens

from ply import *
# ------------------------------------
# definitions of parsing rules by yacc
# ------------------------------------
precedence = (
    )
names = {}

def p_body(p):
    '''body : statement'''
    print '<body>' + p[1] + '</body>'

def p_state(p):
    '''statement : expression
            | statement CR expression'''
    if (len(p)==2):
        p[0] = p[1]
    elif (len(p) == 4):
        p[0] = str(p[1]) + '<br>' + str(p[3])

def p_exp_cr_1(p):
    '''expression : H1 factor'''
    p[0] = '<h1>' + str(p[2]) + '</h1>'

def p_exp_cr_2(p):
    '''expression : H2 factor'''
    p[0] = '<h2>' + str(p[2]) + '</h2>'

def p_exp_cr3(p):
    '''expression : H3 factor'''
    p[0] = '<h3>' + str(p[2]) + '</h3>'


def p_exp_cr(p):
    '''expression : factor'''
    p[0] = p[1]

def p_factor_text(p):
    "factor : text"
    p[0] = p[1]

def p_text_word(p):
    '''text : WORD
        | BLANK text
        | WORD text
        '''
    if len(p)==3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_error(p):
    if p:
        print("error at '%s' line '%d'" % (p.value, p.lineno))
    else:
        print("error at EOF")
        
yacc.yacc(debug=0)