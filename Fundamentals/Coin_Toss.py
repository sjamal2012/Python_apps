def toss():
    h = 0
    t = 0
    for i in range(1,5001):
        side = ""
        import random
        x = random.uniform(0,0.5)
        y = random.uniform(0.5, 1)
        x_rounded = round(x)
        y_rounded = round(y)
        z = random.uniform(0,1)
        z_rounded = round(z)
        if z_rounded == x_rounded:
            side = "head"
            h += 1
        elif z_rounded == y_rounded:
            side = "tail"
            t += 1
        print "Attempt #" + str(i) + ": Throwing a coin... It's a " + side + "! ... Got " + str(h) + " head(s) so far and " + str(t) + " tail(s) so far"
print "Starting the program..."
toss()
