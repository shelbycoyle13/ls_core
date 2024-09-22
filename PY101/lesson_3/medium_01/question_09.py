# Consider these two simple functions:

def foo(param="no"):
    return "yes"        #returns yes

def bar(param="no"):
    return (param == "no") and (foo() or "no")

# What will the following function invocation return?

bar(foo())

#foo() -> "yes"

# bar("yes") -> (param == "no") and (foo() or "no")
#                False        and   ("yes" or "no")     #Technically, as soon as we see False on the left side of the and operator, this it                                                     immediately short circuits. No need to evaluate the right side. (But good practice!)
#                False        and           ("yes")
#                False                                  # returns False!        