name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    if len(favorite_animal) >= len(name):

        for i in range(len(name)):

            new_dict[name[i]] = favorite_animal[i]

    else:
        for i in range(0, len(favorite_animal)):
            new_dict[favorite_animal[i]] = name[i]
    print new_dict
make_dict(name, favorite_animal)
