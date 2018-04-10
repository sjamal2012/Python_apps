class MathDojo(object):
    def __init__(self, x = 0):
        self.x = x

    def add(self, *num):
        total_sum = 0
        for n in num:
            # print type(n) to determine if taking correct type of values
            print type(n)
            if isinstance(n, list):
                list_total = 0
                for value in n:
                    list_total += value
                total_sum += list_total
            else:
                total_sum += n
        self.x += total_sum
        return self

    def subtract(self, *num):
        total_subtract = 0
        for n in num:
            print type(n)
            if isinstance(n, list):
                list_total = 0
                for value in n:
                    list_total += value
                total_subtract -= list_total
            else:
                total_subtract -= n
        self.x += total_subtract
        return self

    def result(self):
        print str(self.x)

md1 = MathDojo()
md1.add(2).add(2,5).subtract(3,2).result()

md2 = MathDojo()
md2.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
