def odd_even():
    for i in range(1, 2001):
        type_num = ""
        if i%2 == 0:
            type_num = "even"
        else:
            type_num = "odd"
        print "Number is " + str(i) + ". This is an " + type_num + " number."
odd_even()
