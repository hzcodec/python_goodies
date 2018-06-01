# The get() method on dicts
# and its "default" argument

#When "get()" is called it checks if the given key exists in the dict.
#If it does exist, the value for that key is returned.
#If it does not exist then the value of the default argument is returned instead.


name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

print greeting(382)

print greeting(333)
