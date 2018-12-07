# https://realpython.com/python-string-split-concatenate-join/

# Avoid this:
print str.split('a,b,c', ',')

#This is bulky and unwieldy when you compare it to the preferred usage:

# Do this instead:
print 'a,b,c'.split(',')
