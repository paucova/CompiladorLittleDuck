grammar littleDuck;

// Tokens
CTE_STRING : '"'~["]*'"';
CTE_INT : '0'|[1-9][0-9]*;
CTE_FLOAT : ('0'|[1-9][0-9]*)'.'[0-9]+;

T_INT : 'int';
T_FLOAT : 'float';
VAR : 'var';
PRINT : 'print';
WHILE : 'while';
DO : 'do';
IF : 'if';
ELSE : 'else';
VOID : 'void';
PROGRAM : 'program';
MAIN : 'main';
END : 'end';

COMMA : ',';
SEMICOLON : ';';
COLON : ':';
ASSIGN : '=';

PLUS : '+';
MINUS : '-';
MULTIPLY : '*';
DIVIDE : '/';
LESS : '<';
GREATER : '>';
NOT_EQUAL : '!=';
EQUAL : '==';
R_PAREN : ')';
L_PAREN : '(';
R_KEY : '}';
L_KEY : '{';
R_BRACKET : ']';
L_BRACKET : '[';

ID : [a-zA-Z][a-zA-Z0-9_]*;

IGNORE : [ \t\r\n]+ -> skip;



// Reglas sintacticas - analisis sintactico

program : PROGRAM ID SEMICOLON vars? funcs* MAIN body END;
body : L_KEY statement+ R_KEY;
type : T_INT | T_FLOAT;
// actualizamos vars para su lectura
vars : VAR var_group+;
var_group : ID (COMMA ID)* COLON type SEMICOLON;

inner_funcs : ID COLON type (COMMA ID COLON type)*;
funcs : VOID ID L_PAREN inner_funcs? R_PAREN L_BRACKET vars body R_BRACKET SEMICOLON;
statement : assignment | condition | cycle | f_call | print;

expression_multiple : expression (COMMA expression)*;
assignment : ID ASSIGN expression SEMICOLON;
condition : IF L_PAREN expression R_PAREN body (ELSE body)? SEMICOLON;
cycle : WHILE L_PAREN expression R_PAREN DO body SEMICOLON;
f_call : ID L_PAREN expression_multiple? R_PAREN SEMICOLON;
print : PRINT L_PAREN (CTE_STRING|expression) (COMMA (CTE_STRING|expression))* R_PAREN SEMICOLON;

expression : exp ((LESS | GREATER | EQUAL | NOT_EQUAL) exp)?;
exp : term ((PLUS | MINUS) term)*;
term : factor ((MULTIPLY | DIVIDE) factor)*;
num_construct : (PLUS | MINUS)? (CTE_INT | CTE_FLOAT);
factor : L_PAREN expression R_PAREN | num_construct | ID;