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
    '''statement :  expression 
    | statement expression '''
    if (len(p)==2):
        p[0] = p[1]
    else: 
        p[0] = p[1] + p[2]

def p_exp_cr_1(p):
    '''expression : H1 factor CR'''
    p[0] = '<h1>' + str(p[2]) + '</h1>'

def p_exp_cr_2(p):
    '''expression : H2 factor CR'''
    p[0] = '<h2>' + str(p[2]) + '</h2>'

def p_exp_cr3(p):
    '''expression : H3 factor CR'''
    p[0] = '<h3>' + str(p[2]) + '</h3>'

def p_exp_cr(p):
    '''expression : lines'''
    p[0] = '<p>' + p[1] + '<\p>'

def p_lines_factor(p):
    '''lines : lines factor
        | lines factor CR
        | factor
    '''
    if(len(p) == 3):
        p[0] = p[1] + p[2]
    elif(len(p) == 4):
        p[0] = p[1] + p[2] + ' '
    else:
        p[0] = p[1]

def p_factor_TEXT(p):
    '''factor : TEXT'''
    p[0] = p[1]

#def p_factor_CR(p):
#    "factor : CR"
    #p[0] = '<br/>'

def p_emfactor_TEXT(p):
    '''factor : STAR TEXT STAR
        | UL TEXT UL '''
    p[0] = '<em>' + str(p[2]) + '</em>'

def p_strongfactor_TEXT(p):
    '''factor : DOUBLESTAR TEXT DOUBLESTAR
        | DUL TEXT DUL '''
    p[0] = '<strong>' + str(p[2]) + '</strong>'


def p_hr(p):
    '''expression : SUB CR
        | SUB
        | EQL CR
        | EQL
    '''
    p[0] = '<hr/>'

#def p_TEXT_word(p):
#    '''TEXT : WORD
#        | TEXT BLANK TEXT
#        | WORD TEXT
#        '''
#    if len(p)==3:
#        p[0] = p[1] + p[2]
#    elif len(p)==2:
#        p[0] = p[1]
#    else:
#        p[0] = p[1] + p[2] + p[3]

def p_error(p):
    if p:
        print("error at '%s' line '%d'" % (p.value, p.lineno))
    else:
        print("error at EOF")
        
yacc.yacc(debug=1)