## Parse tree nodes for the GROVER language

var_table = {}

class Expr:
    pass # empty class 
    
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
            raise ValueError("GROVER: expected axpression but recieved " + str(type(self.child1)))

        if not isinstance(self.child2, Expr):
            raise ValueError("GROVER: expected axpression but recieved " + str(type(self.child2)))

    def eval(self):
        return self.child1.eval() + self.child2.eval()
        
        
class Subtraction(Expr):
    def __init__(self, child1, child2):
        self.child1 = child1
        self.child2 = child2

        if not isinstance(self.child1, Expr):
            raise ValueError("GROVER: expected expression but recieved " + str(type(self.child1)))

        if not isinstance(self.child2, Expr):
            raise ValueError("GROVER: expected expression but recieved " + str(type(self.child2)))

    def eval(self):
        return self.child1.eval() - self.child2.eval()
        
        
class Name(Expr):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name 

    def eval(self):
        if self.name in var_table:
            return var_table[self.name]
        else:
            raise ValueError("GROVER: undefined variable " + self.name)
        
class Stmt:
    def __init__(self, varname, expr):
        self.varname = varname
        self.expr = expr

        if not isinstance(self.expr, Expr):
            raise ValueError("GROVER: expected expression but recieved " + str(type(self.expr)))

        if not isinstance(self.varname, Name):
            raise ValueError("GROVER: expected variable name but recieved " + str(type(self.varname)))

    def eval(self):
        var_table[self.varname.getName()] = self.expr.eval()


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
