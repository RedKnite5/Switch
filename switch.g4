grammar switch;

switch_file  : (line | while_loop)* EOF ;


while_loop  : while_test while_block                                ;
while_test  : WHILE_LOOP_DELIM expr                                 ;
while_block : BLOCK_DELIM (line | while_loop)* WHILE_LOOP_END       ;

line  :  ( (expr | while_loop) EOF | (expr | while_loop)? ENDLINE ) ;

expr  : ( prim_expr
		| call
		| math_op
		| assignment
		| access
		| function
)       ;


function   : FUNCTION_DELIM (NAME (ARG_DELIM NAME)*)?
			 BLOCK_DELIM line* FUNCTION_END             ;

call       : CALL_OP expr (ARG_DELIM args)? END_CALL ;
math_op    : MATH_OPS args END_CALL ;
assignment : ASSIGNMENT_OP (NAME | access) ARG_DELIM expr END_CALL ;
access     : ACCESS_OP expr ARG_DELIM expr (ARG_DELIM expr)* END_CALL ;

args : expr (ARG_DELIM expr)* ;

prim_expr    : ( INT | FLOAT | NAME | STRING ) ;

STRING : STRING_START WHITESPACE* INT (NEXT_CHAR WHITESPACE* INT)* ;

WHITESPACE : (' '|'\t'|'\n'|'\r') -> skip ;

ENDLINE   : 'L' ;
ARG_DELIM : 'n' ;
END_CALL  : 'l' ;

fragment ONE   : ( [oO] )   ;
fragment ZERO  : ( [zZ] )   ;

MATH_OPS     : ( [tvupmjgq] )  ;
ASSIGNMENT_OP  : 'e'        ;
ACCESS_OP      : 'i'        ;
CALL_OP        : 'c'        ;

BLOCK_DELIM : 'B' ;

WHILE_LOOP_DELIM  : 'W'  ;
WHILE_LOOP_END    : 'w'  ;

FUNCTION_DELIM    : 'F'  ;
FUNCTION_END      : 'f'  ;

STRING_START : 'S' ;
NEXT_CHAR    : 's' ;

INT    : ( ONE | ZERO) (ONE | ZERO | WHITESPACE)*   ;
FLOAT  : INT 'd' INT      ;

fragment CHAR : [`~!@#$%^&*()\-_=+{[}\]\\|;:'",<.>/?] ;

NAME : ( CHAR+ ) ;
