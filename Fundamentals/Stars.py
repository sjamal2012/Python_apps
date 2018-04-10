x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(array):
    for i in range(0, len(x)):
        if type(x[i]) == str:
            print x[i][0] * len(x[i])
        else:
            print "*" * x[i]
draw_stars(x)
