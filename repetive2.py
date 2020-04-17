from bisect import bisect 

def func1():
	print('func1 selected')

def func2():
	print('func2 selected')

def func3():
	print('func3 selected')

def to_hi():
	print('to_hi selected')

def to_low():
	print('to_low selected')

def grade(score, breakpoints=[60, 70, 80, 90], grades=[to_low, func1, func2, func3, to_hi]):
     i = bisect(breakpoints, score)
     return grades[i]()


grade(55)   # to_low selected
grade(65)   # func1 selected
grade(75)   # func2 selected
grade(85)   # func3 selected
grade(95)   # to_hi selected

