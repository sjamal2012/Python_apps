l = ['magical unicorns',19,'hello',98.98,'world']
sentence = ""
sum = 0
typeStr = 0
typeInt = 0
for item in l:
    if isinstance(item, str):
        sentence += " " + item
        typeStr += 1
    if isinstance(item, int) or isinstance(item, float):
        sum += item
        typeInt += 1

if typeStr > 0 and typeInt == 0:
    print "The list you entered is of string type"
    print "Sentence: " + sentence
if typeStr == 0 and typeInt > 0:
    print "The list you entered is of integer type"
    print "Sum: " + str(sum)
if typeStr > 0 and typeInt > 0:
    print "The list you entered is of mixed type"
    print "String:" + sentence
    print "Sum: " + str(sum)
