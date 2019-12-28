import numpy as np

def gen_rd_arr(l):
    return np.random.randint(0, 1000, l)

def sort_bubble(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def sort_merge(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        sort_merge(L)
        sort_merge(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1


l = [3,2,7,5,7,9]
s = l[:]
s.sort()
print(list(np.sort(l)))
print(l)
print(s)

# a = list(gen_rd_arr(100))
# print(a)
# sort_merge(a)
# print(a)