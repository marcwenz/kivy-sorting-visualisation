from sorting import sort
import random as rd

l = [rd.randint(1, 10) for _ in range(10)]

print(sort(l, 'merge'))