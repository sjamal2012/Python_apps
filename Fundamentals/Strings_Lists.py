words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
month = words.replace("day", "month")
print month

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98, "world"]
first = x[0]
last = x[len(x) - 1]
print first, last

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = x[0:(len(x)/2)]
for i in range(0, (len(x)/2)):
    x.pop(0)

x.insert(0,y)

'''
while loop performing the above function:

    i = 0
    while i < (len(x)/2):
        x.pop(i)
        i += 1
'''
print x
