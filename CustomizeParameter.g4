grammar CustomizeParameter;

function
  : CUSTOMIZE_PREFIX ('.'? IDENTITIER)+
  | CUSTOMIZE_PREFIX functionObject
  ;

functionObject
  : '"' IDENTITIER '"'                  // string
  | IDENTITIER                          // object
  ;

// lexer and fragment
IDENTITIER
  : (LETTER | DIGIT | '_')+
  ;

STRING
  : LETTER+
  ;
NUMBER
  : DIGIT+
  ;

WS
  : [ \r\n\t]+ -> channel(HIDDEN)       // only for skip rule
  ;

// fragment
fragment CUSTOMIZE_PREFIX
  : [$]
  ;
fragment LETTER
  : [a-zA-Z]
  ;
fragment DIGIT
  : [0-9]
  ;