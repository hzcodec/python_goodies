person = {'name':'Jennie', 'age':16}
person_list = ['Kalle', 44]

sentence = '(A) My name is {} and I am {} years old.'.format(person['name'], person['age'])
print sentence
print 50*'='


sentence = '(B) My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print sentence
print 50*'='

tag = 'hi'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print sentence
print 50*'='


sentence = '(C) My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
print sentence
print 50*'='

sentence = '(D) My name is {0[name]} and I am {0[age]} years old.'.format(person)
print sentence
print 50*'='

sentence = '(E) My name is {0[0]} and I am {0[1]} years old.'.format(person_list)
print sentence
print 50*'='


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Nisse', 50)

sentence = '(F) My name is {0.name} and I am {0.age} years old.'.format(p1)
print sentence
print 50*'='


sentence = '(G) My name is {name} and I am {age} years old.'.format(name='Jennie', age='12') 
print sentence
print 50*'='


# this is supercalifragilisticexpialidocious
sentence = '(H) My name is {name} and I am {age} years old.'.format(**person) 
print sentence
print 50*'='


for i in range(1, 11):
    sentence = 'The value is {}'.format(i)
    print sentence
print 50*'='
for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)
    print sentence

print 50*'='
pi = 3.141592654
sentence = 'Pi is equal to {:.2f}'.format(pi)
print sentence

sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print sentence
print 50*'='

import datetime
my_date = datetime.datetime(2018, 03, 30, 20, 28, 30)
print(my_date)
print 50*'='

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)


