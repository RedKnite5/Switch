grammar switch;

expr  : ( prim_expr
		| call
		| m_expr
		| add_sub_expr
		| assignment
		| access 
		| comp )       ;

call    : 'c' expr 'n' args 'l' ;
m_expr       : MATH_OPS_M args ;
add_sub_expr : MATH_OPS_A args ;
assignment   : 'e' (NAME | access) 'n' expr ;
access       : 'i' args ;
comp         : COMPARISON_OPS args ;

args : expr ('n' expr )* ;

prim_expr    : ( INT | FLOAT | NAME | STRING ) ;

STRING : 'S' INT ('s' INT)* ;

WHITESPACE : (' '|'\t'|'\n'|'\r') -> skip ;

fragment ONE   : ( [oO]  )  ;
fragment ZERO  : ( [zZ]  )  ;

MATH_OPS_M     : ( [tvu] )  ;
MATH_OPS_A     : ( [pm]  )  ;
COMPARISON_OPS : ( [lgq] )  ;

INT    : ( ONE | ZERO )+  ;
FLOAT  : INT 'd' INT      ;

fragment CHAR : [`~!@#$%^&*()\-_=+{[}\]\\|;:'",<.>/?] ;

NAME : ( CHAR+ ) ;
