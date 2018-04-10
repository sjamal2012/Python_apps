# prints all odd numbers from 1 to 1000
for odd in range(1, 1000):
    if odd % 2 != 0:
        print odd

# prints all multiples of 5 from 5 to 1,000,000
for mult in range(5, 1000000):
    if mult % 5 == 0:
        print mult

# prints the sum of all values in list a
totalSum = 0
a = [1, 2, 5, 10, 255, 3]
for i in range(0, 5):
    totalSum += a[i]
print totalSum

# prints the average of the values in a
print totalSum / len(a)
