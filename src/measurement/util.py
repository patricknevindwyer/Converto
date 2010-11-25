'''
Created on Nov 24, 2010

@author: patricknevindwyer

The measurement method is a decorator for setting required types in a function call.
'''


# base example for start of required type decorator
class reqDecorator(object):
    def __init__(self, *kargs):
        print "Decorating"
        for arg in kargs:
            print "dec arg: ", arg
    def __call__(self, f):
        def newf(*kargs, **kwargs):
            print "calling decorated method"
            return f(*kargs, **kwargs)
        return newf
            

@reqDecorator("aaa", "bbb")
def myfunc(a, b):
    print "from myfunc: %s, %s" % (a, b)
    
    
# ideal would be to mark a method with
@measurement(Length, Area, Float)
def scaleVolume(l, a, f):
    return l * a * f
