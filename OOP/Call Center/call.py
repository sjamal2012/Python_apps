from datetime import datetime
time = datetime.now().strftime("%I:%M:%S %p")
class Call(object):
    def __init__(self, unique_id, name_caller, number_caller, time_call, reason_call):
        self.unique_id = unique_id
        self.name_caller = name_caller
        self.number_caller = number_caller
        self.time_call = time_call
        self.reason_call = reason_call

    def display(self):
        d = {}
        d['id'] = self.unique_id
        d['name'] = self.name_caller
        d['number'] = self.number_caller
        d['time'] = self.time_call
        d['reason_call'] = self.reason_call
        return d



class CallCenter(Call):
    def __init__(self, calls=[], queue_size=0):
        self.calls = calls
        self.queue_size = queue_size

    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self

    def remove(self):
        self.calls.pop(0)
        return self

    def info(self):
        # print Call.name_caller
        print self.calls
        print self.queue_size

call1 = Call(1, "Sammy", 1234, time, "bored").display()
call2 = Call(2, "Sarah", 4321, time, "sad").display()

calls = CallCenter()
#testing if add function adds to queue as well as adds new call dictionary
calls.add(call1).add(call2)

#tesing if remove function revmoes first call in list
calls.remove()

print calls.info()
