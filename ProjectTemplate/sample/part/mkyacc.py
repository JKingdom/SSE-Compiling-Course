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
    '''expression : H1 factor cr'''
    p[0] = '<h1>' + str(p[2]) + '</h1>'

def p_exp_cr_2(p):
    '''expression : H2 factor cr'''
    p[0] = '<h2>' + str(p[2]) + '</h2>'

def p_exp_cr3(p):
    '''expression : H3 factor cr'''
    p[0] = '<h3>' + str(p[2]) + '</h3>'

def p_exp_cr(p):
    '''expression : lines'''
    p[0] = '<p>' + p[1] + '</p>'

def p_exp_block(p):
    '''expression : block'''
    p[0] = '<block>' + p[1] + '</block>'


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
        | lines cr
        | factor
    '''
    if(len(p) == 3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_block(p):
    '''block : block bline
    | bline
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_bline(p):
    ''' bline : RIST lines cr
    '''
    p[0] = p[2]


def p_factor_text(p):
    '''factor : text'''
    p[0] = p[1]

#def p_factor_cr(p):
#    "factor : cr"
#    p[0] = '<br/>'

def p_emfactor_text(p):
    '''factor : STAR factor STAR'''
    p[0] = '<em>' + str(p[2]) + '</em>'

def p_strongfactor_text(p):
    '''factor : DOUBLESTAR factor DOUBLESTAR'''
    p[0] = '<strong>' + str(p[2]) + '</strong>'

def p_code_text(p):
    '''factor : POINT factor POINT '''
    p[0] = '<code>' + str(p[2]) + '</code>'

def p_text_TEXT(p):
    '''text : TEXT
    | text NUMBER
    | text TEXT
    '''
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]


def p_lrsm(p):
    '''factor : LEMI factor RIMI LESM factor RISM'''
    p[0] = '<a href="' + str(p[5]) + '">' + str(p[2]) + '</a>'


def p_lrst(p):
    '''factor : LEST factor RIST'''
    p[0] = '<a href="' + str(p[2]) + '">' + str(p[2]) + '</a>'


def p_hr(p):
    '''expression : HR cr
    '''
    p[0] = '<hr/>'


def p_ex_ul(p):
    '''expression : ul '''
    p[0] = '<ul>' + p[1] + '</ul>'


def p_ex_ol(p):
    '''expression : ol'''
    p[0] = '<ol>' + p[1] + '</ol>'



def p_ul(p):
    '''ul : ul li
        | li
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_seul(p):
    '''seul : seul seli
        | seli
    '''
    if len(p) == 3:
        p[0] = str(p[1]) + str(p[2])
    else:
        p[0] = p[1]



def p_li(p):
    '''li : LI factor cr
        | seul
    '''
    if len(p)==4:
        p[0] = '<li>' + str(p[2]) + '</li>'
    else:
        p[0] = '<ul>' + p[1] + '</ul>'



def p_seli(p):
    '''seli : SELI factor cr
        | trul
    '''
    if len(p) == 4:
        p[0] = '<li>' + str(p[2]) + '</li>'
    else:
        p[0] = '<ul>' + p[1] + '</ul>'


def p_trul(p):
    '''trul : trul trli
        | trli
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_trli(p):
    '''trli : TRLI factor cr
    '''
    p[0] = '<li>' + str(p[2]) + '</li>'


def p_ol(p):
    '''ol : ol nli
        | nli
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_nli(p):
    '''nli : NLI factor cr
    | seul'''
    if len(p)==4:
        p[0] = '<li>' + str(p[2]) + '</li>'
    else:
        p[0] = '<ul>' + str(p[1]) + '</ul>'

def p_cr_T(p):
    '''cr : CR
    | T cr
    | cr CR
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


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