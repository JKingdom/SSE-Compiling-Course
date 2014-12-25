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
    p[0] = '<p>' + p[1] + '</p>'

# code start
def p_code_codeline(p):
    '''expression : code
    | expression codeline
    '''
    if(len(p) == 2):
        p[0] = '<code>'+'<ol>'
    else:
        p[0] = p[1] + '<li>' + p[2]+'</li>' 

def p_code_end(p):
    "expression : expression rbrace"
    p[0] = p[1] + '</ol>' + '</code>'

#code end

def p_lines_factor(p):
    '''lines : lines factor
        | lines CR
        | factor
    '''
    if(len(p) == 3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_factor_TEXT(p):
    '''factor : TEXT'''
    p[0] = p[1]

#def p_factor_CR(p):
#    "factor : CR"
    #p[0] = '<br/>'

def p_emfactor_TEXT(p):
    '''factor : STAR TEXT STAR'''
    p[0] = '<em>' + str(p[2]) + '</em>'

def p_strongfactor_TEXT(p):
    '''factor : DOUBLESTAR TEXT DOUBLESTAR'''
    p[0] = '<strong>' + str(p[2]) + '</strong>'

def p_code_TEXT(p):
    '''factor : CODE TEXT CODE'''
    p[0] = '<code>' + str(p[2]) + '</code>'


def p_lrsm(p):
    '''factor : LEMI factor RIMI LESM factor RISM'''
    p[0] = '<a href="' + str(p[5]) + '">' + str(p[2]) + '</a>'


def p_lrst(p):
    '''factor : LEST factor RIST'''
    p[0] = '<a href="' + str(p[2]) + '">' + str(p[2]) + '</a>'


def p_hr(p):
    '''expression : HR CR
    '''
    p[0] = '<hr/>'


def p_ex_ul(p):
    '''expression : ul CR'''
    p[0] = '<ul>' + p[1] + '</ul>'


def p_ex_ol(p):
    '''expression : ol CR'''
    p[0] = '<ol>' + p[1] + '</ol>'



def p_ul(p):
    '''ul : ul CR li
        | li
    '''
    if len(p) == 4:
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1]



def p_ol(p):
    '''ol : ol CR nli
        | nli
    '''
    if len(p) == 4:
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1]



def p_li(p):
    '''li : LI factor
        | STAR factor
    '''
    p[0] = '<li>' + str(p[2]) + '</li>'

def p_nli(p):
    '''nli : NLI factor'''
    p[0] = '<li>' + str(p[2]) + '</li>'


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

# Declare the state
states = (
  ('code','exclusive'),
)


        
yacc.yacc(debug=1)