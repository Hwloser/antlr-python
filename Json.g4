grammar Json;

// run command
// antlr4 -Dlanguage=Python3 Json.g4 -visitor -o antlr

json
  : (object(','?))+
  ;

object
  : '{' pair (',' pair)* '}'
  | '{' '}'
  ;

pair
  : '"' STRING '"' ':' pairValues
  ;

pairValues
  : '"' value '"'
  | ('"' value '"' '+')* function ( '+' '"' value '"')*
  ;

array
  : '[' value (',' value)* ']'
  | '[' ']'
  ;

value
  : STRING
  | NUMBER
  | object
  | array
  | 'true'
  | 'false'
  | 'null'
  ;

// embeded function
function
  : functionName '(' ')'                                    // empty function
  | functionName '(' (argument(','?))+ ')'                  // function
  | functionName '(' function+  ')'                         // embeded function
  ;

argument
  : STRING
  | NUMBER
  ;

functionName
  : '$'? (STRING('.'?))+
  ;

// function type
STRING
  : [a-zA-Z]+
  ;
NUMBER
  : [0-9]+
  ;

// only for skip rule
WS
  : [ \t\n\r] + -> skip
  ;
