grammar switch;

switch_file  : line* EOF ;


while_loop  : while_test while_block                                ;
while_test  : WHILE_LOOP_DELIM expr                                 ;
while_block : BLOCK_DELIM line* WHILE_LOOP_END                      ;


line: non_func_line | func_line ;

non_func_line  :  statement EOF | (statement? ENDLINE) | while_loop ;

func_line      :  func_statement | (func_statement? ENDLINE) ;

func_statement : statement | return_statement ;
statement : expr | while_loop ;

return_statement  : FUNCTION_RETURN (expr)? ;

expr  : ( prim_expr
		| call
		| math_op
		| assignment
		| access
		| function
)       ;


function   : FUNCTION_DELIM (NAME (ARG_DELIM NAME)*)?
			 BLOCK_DELIM func_line* FUNCTION_END             ;

call       : CALL_OP expr (ARG_DELIM args)? END_CALL ;
math_op    : MATH_OPS args END_CALL ;
assignment : ASSIGNMENT_OP (NAME | access) ARG_DELIM expr END_CALL ;
access     : ACCESS_OP expr ARG_DELIM expr (ARG_DELIM expr)* END_CALL ;

args : expr (ARG_DELIM expr)* ;

prim_expr    :  INT | FLOAT | NAME | STRING  ;

STRING : STRING_START WHITESPACE* INT (NEXT_CHAR WHITESPACE* INT)* ;

WHITESPACE : (' '|'\t'|'\n'|'\r') -> skip ;

ENDLINE   : 'L' ;
ARG_DELIM : 'n' ;
END_CALL  : 'l' ;

fragment ONE   : ( [oO] )   ;
fragment ZERO  : ( [zZ] )   ;

MATH_OPS       : ( [tvupmjgq] )  ;
ASSIGNMENT_OP  : 'e'             ;
ACCESS_OP      : 'i'             ;
CALL_OP        : 'c'             ;

BLOCK_DELIM       : 'B'    ;

WHILE_LOOP_DELIM  : 'W'    ;
WHILE_LOOP_END    : 'w'    ;

FUNCTION_DELIM    : 'F'    ;
FUNCTION_END      : 'f'    ;

FUNCTION_RETURN   : 'ret'  ;

STRING_START : 'S' ;
NEXT_CHAR    : 's' ;

INT    : ( ONE | ZERO) (ONE | ZERO | WHITESPACE)*   ;
FLOAT  : INT 'd' INT                                ;

fragment CHAR : [`~!@#$%^&*()\-_=+{[}\]\\|;:'",<.>/?] ;

NAME : ( CHAR+ ) ;
