## Parse tree nodes for the GROVER language

var_table = {}

class Expr:
    pass # empty class

class Str(Expr):
    def __init__(self, value):
        self.value = value

        noWhite = value.split()
        if len(noWhite) > 1:
            GroverError("GROVER: no spaces allowed on Strings")
        noQuotes = value.split('"')
        if len(noQuotes) > 1:
           GroverError("GROVER: no support for quotes in Strings")

    def eval(self):
        return self.value
    
class Num(Expr):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

        
class Addition(Expr):
    def __init__(self, child1, child2):
        self.child1 = child1
        self.child2 = child2

        if not isinstance(self.child1, Expr):
            raise GroverError("GROVER: expected axpression but recieved " + str(type(self.child1)))

        if not isinstance(self.child2, Expr):
            raise GroverError("GROVER: expected axpression but recieved " + str(type(self.child2)))

        if type(self.chidl1) != type(self.child2):
            raise GroverError("GROVER: arguemnts are not of the same type")

    def eval(self):
        return self.child1.eval() + self.child2.eval()
        
#TODO: create a class "call"
# Double check for what type of arguments
class Call(Expr):
    def __init__(self, obj, method, *args, **kwargs):
        self.obj = obj
        self.method = method

        if method not in dir(obj) and callable(getattr(obj,method)):
            raise GroverError("GROVER: " + obj + " does not contain method " + method)

    #TODO: understand how *args **kwargs work and how to loop through them

    def eval(self):
        pass
        

#TODO: create Str class
#Split on white spaces, then check for length if 1 split on quotes and check for length. Lastly, evalutate string
        
        
class Name(Expr):
    def __init__(self, name):
        self.name = name

    #TODO: add the extra conditions
    if (!name[0].isalpha() and name[0] != "_"):
        raise GroverError("GROVER: " + name + " is invalid sytax for the name of a variable")

    def getName(self):
        return self.name 

    def eval(self):
        if self.name in var_table:
            return var_table[self.name]
        else:
            raise ValueError("GROVER: undefined variable " + self.name)

#TODO: understand the differences between "set" and "new" and update accordingly
class Stmt:
    def __init__(self, varname, expr, isSet):
        self.varname = varname
        self.expr = expr

        if not isinstance(self.expr, Expr):
            raise ValueError("GROVER: expected expression but recieved " + str(type(self.expr)))

        if not isinstance(self.varname, Name):
            raise ValueError("GROVER: expected variable name but recieved " + str(type(self.varname)))

    def eval(self):
        if (isSet):
            var_table[self.varname.getName()] = self.expr.eval()
        #else:
            #var_table[self.varname.getName()] = 


class GroverError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

# # some testing code
# if __name__ == "__main__":
#     assert(Num(3).eval() == 3)
#     assert(Addition(Num(3), Num(10)).eval() == 13)
#     assert(Subtraction(Num(3), Num(10)).eval() == -7)
#     assert(Div(Num(10), Num(2)).eval() == 5)
#     assert(Mult(Num(3), Num(4)).eval() == 12)
    
#     caught_error = False
#     try:
#         print(Name("nope").eval())
#     except ValueError:
#         caught_error = True
#     assert(caught_error)
    
#     assert(Stmt(Name("foo"), Num(10)).eval() is None)
#     assert(Name("foo").eval() == 10)
    
#     # Try something more complicated
#     assert(Stmt(Name("foo"), Addition(Num(200), Subtraction(Num(4), Num(12)))).eval() is None)
#     assert(Name("foo").eval() == 192)
