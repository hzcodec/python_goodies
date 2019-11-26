# The get() method on dicts
# and its "default" argument

#When "get()" is called it checks if the given key exists in the dict.
#If it does exist, the value for that key is returned.
#If it does not exist then the value of the default argument is returned instead.


#name_for_userid = {
#    382: "Alice",
#    590: "Bob",
#    951: "Dilbert",
#}

def f1():
    print('Yes')
 

getit = {
    'hello': "there",
    'oh': "shit",
    951: "Dilbert",
    'mark': f1
}

#def greeting(userid):
#    return "Hi %s!" % name_for_userid.get(userid, "there")

def pef(userid):
    return "wtf %s!" % getit.get(userid, "oh no")

#print greeting(382)
#print greeting(333)

print pef('hello')
print pef('jennie')
x = pef('mark')
