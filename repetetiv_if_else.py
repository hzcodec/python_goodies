#
# How can I simplify repetitive if-elif statements?
#
# https://stackoverflow.com/questions/61030617/how-can-i-simplify-repetitive-if-elif-statements

#
# Example 1
#
#from bisect import bisect 
#
#def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect(breakpoints, score)
#     return grades[i]
#
##>>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
#
#print(grade(60))  # D
#print(grade(40))  # F
#print(grade(90))  # A

#
# Example 2
#
def grade(score):
    grades = zip('ABCD', (.9, .8, .7, .6))
    return next((grade for grade, limit in grades if score >= limit), 'F')

print(grade(1))    # A
print(grade(2))    # A
print(grade(.88))  # B
print(grade(.59))  # F
print(grade(.75))  # C
print(grade(.65))  # D


#
# Example 3
#
#Note, if you're using Python 3.6 or below, you should do sorted(grades.items()) 
#      since dicts aren't guaranteed to be sorted.
#grades = {"A": 0.9, "B": 0.8, "C": 0.7, "D": 0.6, "E": 0.5}
#
#def convert_grade(scr):
#    for ltrgrd, numgrd in grades.items():
#        if scr >= numgrd:
#            return ltrgrd
#    return "F"
#
#print(convert_grade(0.8))  # C
#print(convert_grade(1.8))  # A
#print(convert_grade(.49))  # F


#
# Example 4
#

