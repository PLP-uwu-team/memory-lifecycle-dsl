grammar MemoryPolicy;

policy
    : 'track_memory' '{' policyRule* '}' EOF
    ;

// Ganti 'rule' jadi 'policyRule' biar gak konflik
policyRule
    : pairRule
    | transferRule
    ;

pairRule
    : 'pair' '{'
        'allocator' ':' allocator=STRING
        'deallocator' ':' deallocator=STRING
      '}'
    ;

transferRule
    // Ganti 'list' jadi 'functionList'
    : 'transfer_ownership' ':' functionList
    ;

functionList
    : '[' (STRING (',' STRING)*)? ']'
    ;

STRING : '"' (~["\r\n])* '"' ;
COMMENT : '//' ~[\r\n]* -> skip ;
WS     : [ \t\r\n]+ -> skip ;