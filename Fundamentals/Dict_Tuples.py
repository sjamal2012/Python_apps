myDict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
myTuple = []
def dictuple(array):
    for key,value in myDict.iteritems():
        myTuple.append(tuple((key,value)))

dictuple(myDict)
print myTuple
