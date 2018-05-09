## Parse tree nodes for the GROVE language
import importlib
from types import ModuleType

var_table = {}

class Expr:
    pass # empty class

class Imprt(Expr):
    def __init__(self, packname):
        self.packname = packname

    def eval(self):
        try:
            mod = importlib.import_module(self.packname.getName())
        except ImportError as e:
            raise GroveError("GROVE: package does not exist")
        
        if self.packname not in globals().keys():
            globals()[self.packname.getName()] = mod

class Str(Expr):
    def __init__(self, value):
        self.value = value

        noWhite = self.value.split()
        if len(noWhite) > 1:
            raise GroveError("GROVE: no spaces allowed on Strings")
        noQuotes = self.value.split('"')
        if len(noQuotes) == 2:
            raise GroveError("GROVE: missing quotation mark")
        if len(noQuotes) > 3:
            raise GroveError("GROVE: no support for quotes in Strings")
        if not isinstance(self.value, str):
            raise GroveError("GROVE: not a valid String value")

    def eval(self):
        return self.value.strip('"\'')
    
class Num(Expr):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

        
class Addition(Expr):
    def __init__(self, child1, child2):
        self.child1 = child1
        self.child2 = child2

    def eval(self):

        if not isinstance(self.child1, Expr):
            raise GroveError("GROVE: expected axpression but recieved " + str(type(self.child1)))

        if not isinstance(self.child2, Expr):
            raise GroveError("GROVE: expected axpression but recieved " + str(type(self.child2)))

        res1 = self.child1.eval()
        res2 = self.child2.eval()

        if type(res1) != type(res2):
            raise GroveError("GROVE: arguemnts are not of the same type")

        return res1 + res2
        
#TODO: create a class "call"
# Double check for what type of arguments
class Call(Expr):
    def __init__(self, obj, method, *args):
        #rint("IT GETS HERE")
        #print(obj.getName())
        #print(method.getName())
        self.obj = obj
        self.method = method
        self.args = args
        if '=' in self.args[0]:
            raise GroveError("No statements allowed in method call")

    #TODO: understand how *args **kwargs work and how to loop through them

    def eval(self):
        #print("IT GETS HERE")
         # WE ARE TREATING the number 4 as a method, and we can't
        #print(dir(self.obj.getName()))
        if self.method.getName() not in dir(self.obj.getName()):
            #print(self.obj)
            #print(self.method.getName())
            raise GroveError("GROVER: object " + self.obj.getName() + " does not have a method named " + self.method.getName())
        if not callable(getattr(self.obj.getName(), self.method.getName())):
            raise GroveError("GROVER: method " + self.method.getName() + " is not callable")

        f = getattr(self.obj.eval(), self.method.getName())
        
        try:
            if len(self.args[0]) == 0:
                x = f()
                return x
            else:
                y = self.args[0][0]
                y = y.replace('"',"")
                
                #print(y)
                x = f(y)
                return x
        except:
            raise GroveError("GROVE: invalid call syntax")
        #print(f())
        #return f(self.args)

class ComplexName(Expr):
    def __init__(self, name):
        self.name = name
        if self.name.count(".") != 1:
            raise GroveError("GROVE: Wrong class name")

    def eval(self):
        if not self.name[0].isalpha() and name[0] != "_":
            raise GroveError("GROVE: " + name + " is invalid sytax for the name of a class")

        
    
#TODO: Create className & variableName classes
class ClassName(Expr):
    def __init__(self, name):
        self.name = name
        #TODO: add the extra conditions

    def eval(self):
        #if name not in globals():

        if not self.name[0].isalpha() and name[0] != "_":
            raise GroveError("GROVE: " + name + " is invalid sytax for the name of a class")


    def getName(self):
        return self.name
        
#Split on white spaces, then check for length if 1 split on quotes and check for length. Lastly, evalutate string

#Name may have classes not in the vartable yet, change accordingly --- Change this to a like "variableName" and have Name not be evaluated        
class VariableName(Expr):
    def __init__(self, name):
        self.name = name

        #TODO: add the extra conditions
        if not self.name[0].isalpha() and name[0] != "_":
            raise GroveError("GROVE: " + name + " is invalid sytax for the name of a variable")

    def getName(self):
        return self.name 

    def eval(self):
        if self.name in var_table:
            return var_table[self.name]
        else:
            raise GroveError("GROVE: undefined variable " + self.name)

#TODO: understand the differences between "set" and "new" and update accordingly
class Stmt:
    def __init__(self, varname, expr, isSet):
        self.varname = varname
        self.expr = expr
        self.isSet = isSet

    def eval(self):
        if not isinstance(self.expr, Expr):
            raise GroveError("GROVE: expected expression but recieved " + str(type(self.expr)))

        if not isinstance(self.varname, VariableName):
            raise GroveError("GROVE: expected variable name but recieved " + str(type(self.varname)))

        if (self.isSet):
            var_table[self.varname.getName()] = self.expr.eval()
        else:
            #TODO: learn to handle the <Name>.<Name> and <Name>
            
            #FROM WOLVES' CODE
            self.modulename = "__builtins__"
            self.classname = self.expr

            # if isinstance(self.varname.getName(), ModuleType):
            #     cls = getattr(self.varname.getName(), self.classname)
            # else:
            #     cls = self.varname.getName()[self.classname]

            # var_table[self.varname.getName()] = cls()


            if isinstance(self.modulename, ModuleType):
                cls = getattr(self.varname.getName(), self.classname)
            else:
                cls = self.modulename[self.classname]

            var_table[self.varname.getName()] = cls()


class GroveError(Exception):
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
#     except GroveError:
#         caught_error = True
#     assert(caught_error)
    
#     assert(Stmt(Name("foo"), Num(10)).eval() is None)
#     assert(Name("foo").eval() == 10)
    
#     # Try something more complicated
#     assert(Stmt(Name("foo"), Addition(Num(200), Subtraction(Num(4), Num(12)))).eval() is None)
#     assert(Name("foo").eval() == 192)
