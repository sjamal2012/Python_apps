from datetime import datetime
from collections import OrderedDict
time = datetime.now().strftime("%I:%M:%S %p")
class Patient(object):
    def __init__(self, unique_id, name, allergies, bed_num):
        self.unique_id = unique_id
        self.name = name
        self.allergies = allergies
        self.bed_num = bed_num

    def display(self):
        d = OrderedDict()
        d['id'] = self.unique_id
        d['name'] = self.name
        d['allergies'] = self.allergies
        d['bed_num'] = self.bed_num
        return d



class Hospital(Patient):
    def __init__(self, name, capacity, patients=[]):
        self.patients = patients
        self.name = name
        self.capacity = capacity

    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "At capacity"
            return self
        self.patients.append(patient)
        return self

    def discharge(self, patient):
        self.patients.pop(self.patients.index(patient))
        return self

    def info(self):
        print "Hospital: " + str(self.name)
        print "Capacity: " + str(len(self.patients)) + " out of " + str(self.capacity)
        print "Patient list: " + str(self.patients)

pat1 = Patient(1, "Sammy Jamal", "penicillin, ibuprofin", 45).display()
pat2 = Patient(2, "Sarah Jamal", "none", 47).display()


hospital1 = Hospital("Kaiser", 2)
#testing if add function adds to queue as well as adds new call dictionary
hospital1.admit(pat1).admit(pat2)
#testing if discharge function works
hospital1.discharge(pat1)

#print
print hospital1.info()
