grammar switch;

switch_file  : (line | while_loop)* EOF ;

while_loop  : while_test while_block ;
while_test  : 'W' expr               ;
while_block : 'Wb' line* 'w'         ;

line  :  (expr EOF | expr? ENDLINE) ;

expr  : ( prim_expr
		| call
		| mult
		| add_sub_expr
		| assignment
		| access 
		| comp )       ;

call    : 'c' expr ARG_DELIM args 'l' ;
mult       : MATH_OPS_M args ;
add_sub_expr : MATH_OPS_A args ;
assignment   : 'e' (NAME | access) ARG_DELIM expr ;
access       : 'i' expr ARG_DELIM args ;
comp         : COMPARISON_OPS args ;

args : expr (ARG_DELIM expr)* ;

prim_expr    : ( INT | FLOAT | NAME | STRING ) ;

STRING : 'S' WHITESPACE* INT ('s' WHITESPACE* INT)* ;

WHITESPACE : (' '|'\t'|'\n'|'\r') -> skip ;

ENDLINE   : 'L' ;
ARG_DELIM : 'n' ;

fragment ONE   : ( [oO] )   ;
fragment ZERO  : ( [zZ] )   ;

MATH_OPS_M     : ( [tvu] )  ;
MATH_OPS_A     : ( [pm]  )  ;
COMPARISON_OPS : ( [jgq] )  ;

INT    : ( ONE | ZERO) (ONE | ZERO | WHITESPACE)*   ;
FLOAT  : INT 'd' INT      ;

fragment CHAR : [`~!@#$%^&*()\-_=+{[}\]\\|;:'",<.>/?] ;

NAME : ( CHAR+ ) ;
