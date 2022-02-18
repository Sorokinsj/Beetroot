from random import randint
def euclidian_gcd (a, b):
    print("a =", a, "b =", b)
    a = abs (a)
    b = abs (b)
    while a != b:
        if a != 0 or b != 0:
            if a > b:
                a = a - b
            elif a < b:
                b = b - a
        else:
            NOD = 1
    NOD = a
    print ("NOD =", NOD)
    return NOD

if __name__ == "__main__":
    a = randint (-1000, 1000)
    b = randint (-1000, 1000)
    if type(a) == int and type(b) == int:
        euclidian_gcd (a, b)
    else:
        print ('Type is not match')

