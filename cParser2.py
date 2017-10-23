from pyparsing import *

expression =Forward()
statement = Forward()
constant_expression =Forward()
compound_stmnt = Forward()
declaration =Forward()
initializer=Forward()
initializer_list=Forward()
assignment_expression=Forward()
declarator=Forward()
declaration_specifier=Forward()
enumerator_list=Forward()
abstract_declarator=Forward()
direct_abstract_declarator=Forward()
parameter_type_list=Forward()
pointer =Forward()
parameter_list=Forward()
specifier_qualifier=Forward()
conditional_expression=Forward()
unary_expression=Forward()
enumeration_constant =Forward()
character_constant =Forward()
postfix_expression =Forward()
cast_expression=Forward()
expression = Forward()
multiplicative_expression=Forward()
additive_expression=Forward()
shift_expression=Forward()
relational_expression=Forward()
equality_expression=Forward()
and_expression=Forward()
exclusive_or_expression =Forward()
inclusive_or_expression =Forward()
direct_declarator=Forward()
logical_and_expression= Forward()
struct_or_union_specifier=Forward()
logical_or_expression= Forward()
struct_declarator_list= Forward()
type_specifier= Forward()

LPAR,RPAR,LBRACK,RBRACK,LBRACE,RBRACE,SEMI,COMA,EQLTO,LESSTHAN,GRTRTHAN = map(Suppress, "()[]{};,=<>")

INT, CHAR, WHILE, DO, IF, ELSE,FOR, SWITCH,CASE,DEFAULT, RETURN, GOTO, BREAK, CONTINUE,AUTO,REGISTER,STATIC,EXTERN,TYPEDEF = map(Keyword,"int char while do if else for switch case default return goto break continue auto register static extern typedef".split())

SIZEOF,VOID,CHAR,SHORT,INT,LONG,FLOAT,DOUBLE,SIGNED,UNSIGNED,STRUCT,ENUM,UNION, CONST, VOLATILE = map(Keyword,"sizeof void char short int long float double signed unsigned struct enum union const volatile".split())
                
integer_constant = Word(nums) #checked

floating_constant = Word(nums+'.')#checked

storage_class_specifier =  AUTO|REGISTER|STATIC|EXTERN|TYPEDEF #checked

identifier = Word(alphas+'_',alphanums+'_') #checked

break_continue = BREAK|CONTINUE +SEMI #checked

return_stmnt = RETURN + expression +SEMI #checked

jump_stmnt  = GOTO+ identifier + SEMI |break_continue |return_stmnt #checked


iteration_stmnt = Group(WHILE +LPAR+expression+RPAR +LBRACE+ZeroOrMore(statement)+RBRACE|DO+LBRACE+ZeroOrMore(statement)+RBRACE+WHILE+LPAR+expression+RPAR+SEMI|\
                  FOR+LPAR+ZeroOrMore(expression+Optional(SEMI|COMA))+RPAR +LBRACE+ZeroOrMore(statement)+RBRACE)

selection_stmnt =Group(IF+LPAR+expression+RPAR +Optional(LBRACE)+ZeroOrMore(statement)+Optional(RBRACE)\
                       +ZeroOrMore(ELSE+IF+LPAR+expression+RPAR+LBRACE+ZeroOrMore(statement)+RBRACE)\
                       +Optional(ELSE+LPAR+expression+RPAR+ LBRACE+ZeroOrMore(statement)+RBRACE)\
                       |SWITCH+LPAR+expression+RPAR+Literal(':')+LBRACE+ZeroOrMore(statement)+RBRACE)

expression_stmnt = Optional(expression)+SEMI

labeled_stmnt = identifier +Literal(':')+statement|CASE+expression+Literal(':')+statement|DEFAULT+Literal(':')+statement

statement << Group(labeled_stmnt |expression_stmnt|selection_stmnt|iteration_stmnt|jump_stmnt|compound_stmnt)

compound_statement = OneOrMore(ZeroOrMore(declaration) +ZeroOrMore(statement))

initializer_list << initializer|initializer_list+initializer

initializer  << assignment_expression|ZeroOrMore(initializer_list)|ZeroOrMore(initializer_list+COMA)

init_declarator =declarator|declarator +EQLTO+initializer

declaration << OneOrMore(declaration_specifier)+ZeroOrMore(init_declarator)

typedef_name = identifier

enumerator = identifier | identifier +EQLTO+ constant_expression

enumerator_list << enumerator| enumerator_list+ enumerator

enum_specifier= ENUM+ identifier +LBRACE+enumerator_list+RBRACE | ENUM+ LBRACE+enumerator_list+RBRACE | ENUM+ identifier

direct_abstract_declarator <<  Group(abstract_declarator)\
                               | ZeroOrMore(direct_abstract_declarator) +LBRACE+ZeroOrMore(constant_expression)+RBRACE\
                               | ZeroOrMore(direct_abstract_declarator) +ZeroOrMore(parameter_type_list)


abstract_declarator << pointer| pointer+direct_abstract_declarator | direct_abstract_declarator

parameter_declaration= OneOrMore(declaration_specifier)+declarator\
                          | OneOrMore(declaration_specifier)+abstract_declarator\
                          | OneOrMore(declaration_specifier)

parameter_list<< parameter_declaration| parameter_list+parameter_declaration

parameter_type_list<< OneOrMore(parameter_list)

type_name = OneOrMore(specifier_qualifier)+ ZeroOrMore(abstract_declarator)
'''
unary_operator = Literal('&')|Literal('*')|Literal('+')|Literal('-')|Literal('~')|Literal('!')#checked

assignment_operator = Literal('=')|Literal('*=')|Literal('/=')|Literal('%=')|Literal('+=')|Literal('-=')|Literal('<<=')|Literal('>>=')\
                      |Literal('&=')|Literal('^=')|Literal('!=')#checked
                       
assignment_expression << Group(conditional_expression+ assignment_operator+assignment_expression|conditional_expression)#checked

expression << Group(assignment_expression +Optional(COMA)+expression|assignment_expression)#checked
'''
data_type= OneOrMore(INT|CHAR|SHORT|VOID|LONG|FLOAT|DOUBLE|SIGNED|UNSIGNED| struct_or_union_specifier | enum_specifier)
data_type1 = Optional(oneOf("const signed unsigned static register"))+OneOrMore(oneOf("int double char short float long void"))+Optional(Literal('*'))
char = Regex(r"'.'")
string = dblQuotedString
var_value= char|string|Word(alphanums)
expression << (infixNotation(Optional(data_type)+var_value+Optional(LBRACK+ZeroOrMore(Word(nums))+RBRACK),
    [
    (oneOf('! - *'), 1, opAssoc.RIGHT),
    (oneOf('++ --'), 1, opAssoc.RIGHT),
    (oneOf('++ --'), 1, opAssoc.LEFT),
    (oneOf('* / %'), 2, opAssoc.LEFT),
    (oneOf('& ^'), 2, opAssoc.LEFT),
    (oneOf('+ -'), 2, opAssoc.LEFT),
    (oneOf('<< >>'), 2, opAssoc.LEFT),
    (oneOf('<  = == > <= >= !='), 2, opAssoc.LEFT),
    (oneOf('&& |'), 2, opAssoc.LEFT),
    (Regex(r'=[^=]'), 2, opAssoc.LEFT),
    ]) +
    Optional( LBRACK + expression + RBRACK )
    )


constant = integer_constant | character_constant | floating_constant| enumeration_constant

string = Word(alphanums)

'''primary_expression = Group(identifier| constant|string| (LPAR+expression+RPAR))#checked

postfix_expression << Group(primary_expression+LBRACE+expression+RBRACE\
                       | primary_expression +LPAR+ZeroOrMore(assignment_expression)+RPAR\
                       | primary_expression +Literal('.')+identifier\
                       | primary_expression +Literal("->")+identifier\
                       | primary_expression +Literal("++")\
                       | primary_expression +Literal("--")|primary_expression)

unary_expression << Group(Literal("++")+ unary_expression|Literal("--")+ unary_expression| unary_operator+ cast_expression \
                          |SIZEOF +LPAR+type_name+RPAR|SIZEOF + unary_expression|postfix_expression)#Checked

cast_expression << Group((LPAR+type_name+RPAR+cast_expression)|unary_expression)#Checked

multiplicative_expression << Group(cast_expression + Literal('*') + multiplicative_expression\
                              | cast_expression + Literal('/') + multiplicative_expression\
                              | cast_expression + Literal('%') + multiplicative_expression|cast_expression)#checked

additive_expression << Group( multiplicative_expression + Literal('+') + additive_expression\
                        | multiplicative_expression + Literal('-') + additive_expression|multiplicative_expression) #checked


shift_expression << Group(additive_expression + Literal('<<') + shift_expression\
                     | additive_expression + Literal('>>') + shift_expression|additive_expression)#checked

relational_expression << Group( shift_expression + Literal('<') + relational_expression\
                          | shift_expression + Literal('>') + relational_expression\
                          | shift_expression + Literal('<=') + relational_expression\
                          | shift_expression + Literal('>=') + relational_expression|shift_expression)#checked

equality_expression << Group(relational_expression + Literal('==') + equality_expression\
                        | relational_expression + Literal('!=') + equality_expression|relational_expression)#checked        


and_expression << Group(equality_expression + Literal('&') + and_expression|equality_expression) #checked  

exclusive_or_expression << Group(and_expression + Literal('^') + exclusive_or_expression|and_expression) #checked 

inclusive_or_expression << Group(exclusive_or_expression + Literal('|')+inclusive_or_expression|exclusive_or_expression)#checked 


logical_and_expression << Group(inclusive_or_expression + Literal('&&') + logical_and_expression|inclusive_or_expression)#checked


logical_or_expression << Group( logical_and_expression + Literal('||') + logical_or_expression|logical_and_expression)#checked


conditional_expression << Group(logical_or_expression +Literal('?')+ expression +Literal(':')+conditional_expression| logical_or_expression)#checked

constant_expression << conditional_expression#checked


direct_declarator << identifier | LPAR+ declarator+ RPAR| direct_declarator +LBRACE+ZeroOrMore(constant_expression)+RBRACE\
                      | direct_declarator + LPAR +parameter_type_list + RPAR\
                      | direct_declarator + LPAR + ZeroOrMore(identifier) + RPAR

'''
type_qualifier = CONST|VOLATILE
pointer << Literal('*') + ZeroOrMore(type_qualifier)+ ZeroOrMore(pointer)                  

declarator << ZeroOrMore(pointer) + direct_declarator


#struct_declarator = declarator| (declarator + Literal(':')  + constant_expression)| (Literal(':') +  constant_expression)

struct_declarator = declarator| (Optional(declarator) + Literal(':')  + constant_expression)

struct_declarator_list << struct_declarator| struct_declarator_list + struct_declarator

specifier_qualifier << type_specifier| type_qualifier

struct_declaration = ZeroOrMore(specifier_qualifier) + struct_declarator_list

struct_or_union = STRUCT|UNION

struct_or_union_specifier << struct_or_union + identifier +  LBRACE + OneOrMore(struct_declaration) + RBRACE\
                              | struct_or_union +  LBRACE + OneOrMore(struct_declaration) + RBRACE\
                              | struct_or_union + identifier

type_specifier << Group(INT|CHAR|SHORT|VOID|LONG|FLOAT|DOUBLE|SIGNED|UNSIGNED| struct_or_union_specifier | enum_specifier\
                   | typedef_name)

declaration_specifier << Group(storage_class_specifier|type_specifier|type_qualifier)

function_definition= Forward()

function_definition <<ZeroOrMore(declaration_specifier)#+declarator +ZeroOrMore(declaration) +compound_statement

external_declaration= Forward()

translation_unit= Forward()

external_declaration <<function_definition | declaration

translation_unit << ZeroOrMore(external_declaration)

test = r"""
for(int i=0;i<n;i++){
i=0;
short int k[0]=9;
if(i>0&&h<0){int j=0;break;}
while(i<n&&j!=0){double g= 0;return j=0;}}
   """
t=r"""
int main
"""
k= statement.parseString(test)
k.pprint()
#print x.parseString(test)
