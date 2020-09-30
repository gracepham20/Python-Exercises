# input set 1
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = (3, 4, 1, 2, 7, 6, 5, 8)
c = {5, 6, 7, 8, 1, 2, 3, 4}

# input set 2
a1 = [1, 2, 3, 4, 5, 6, 7, 8, 8]
b1 = (3, 4, 1, 2, 7, 6, 5, 8)
c1 = {5, 6, 7, 8, 1, 2, 3, 4}

# input set 3
a2 = [1, 2, 3, 4, 5, 6, 10, 8]
b2 = (3, 4, 1, 2, 7, 6, 5, 8)
c2 = {5, 6, 7, 8, 1, 2, 3, 4}

# input set 4
a3 = []
b3 = ()
c3 = {}


def check(a, b, c):
    b = list(b)
    c = list(c)
    if sorted(a) == sorted(b) == sorted(c):
        return True
    else:
        return False


check(a, b, c)
check(a1, b1, c1)
check(a2, b2, c2)
check(a3, b3, c3)
