myInfo = {"name":"Sammy", "age":"23", "country of birth":"the US", "favorite language":"Python"}
def print_dictionary_values(myInfo):

    for key, value in sorted(myInfo.iteritems()):
        print "My " + key + " is " + value
print_dictionary_values(myInfo)
