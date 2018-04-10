list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5]
if len(list_one) != len(list_two):
    print "The lists are not the same"

else:
    count = 0
    for item in range(0, (len(list_one))):
        if list_one[item] == list_two[item]:
            count += 1
            continue
        else:
            print "The lists are not the same"

    if count == len(list_one):
        print "The lists are the same"
