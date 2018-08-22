# You can get the name of
# an object's class as a
# string:

class MyClass: pass

obj = MyClass()
print obj.__class__.__name__
#'MyClass'

# Functions have a
# similar feature:

def myfunc(): pass

print myfunc.__name__
#'myfunc'
