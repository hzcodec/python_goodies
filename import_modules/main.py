# An empty __init__.py need to be in the directory.
# Make a blank file called __init__.py in your subdirectory (this tells Python it is a module)

import mod1
import sys
import os

#sys.path.insert(0, '/home/heinz.samuelsson/python/import_modules/lib')
#import mod2

#from os.path import dirname, join, abspath
#sys.path.insert(0, abspath(join(dirname(__file__), '..')))
#from lib import mod2
from bsp import mod3, mod4
from lib import mod2


mod1.plot(10, 10)
mod2.calc(12)
mod3.fire()
mod4.done()

comp = mod2.Computer()
comp.calculus()

