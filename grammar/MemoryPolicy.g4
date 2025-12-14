grammar MemoryPolicy;

policy
    : 'track_memory' '{'
        allocateBlock?
        deallocateBlock?
        transferBlock?
      '}'
      EOF
    ;

allocateBlock     : 'allocate_by' ':' list ;
deallocateBlock   : 'deallocate_by' ':' list ;
transferBlock     : 'transfer_ownership' ':' list ;

list
    : '[' (STRING (',' STRING)*)? ']'
    ;

STRING : '"' (~["\r\n])* '"' ;
WS     : [ \t\r\n]+ -> skip ;
