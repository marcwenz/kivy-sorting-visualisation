def sort(arr, type):

    def bubble(arr):
        for i in range(len(arr)-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def rbubble(arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1, i, -1):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    def insertion(arr):
        i = 1
        for i in range(len(arr)):
            j = i
            while j > 0 and arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
        return arr

    def quick(arr, low = 0, high = -1):

        def partition(arr,low,high):
            i = ( low-1 )         # index of smaller element
            pivot = arr[high]     # pivot

            for j in range(low , high):

                # If current element is smaller than the pivot
                if   arr[j] < pivot:

                    # increment index of smaller element
                    i = i+1
                    arr[i],arr[j] = arr[j],arr[i]

            arr[i+1],arr[high] = arr[high],arr[i+1]
            return ( i+1 )

        if high == -1:
            high = len(arr) - 1

        if low < high:

            # pi is partitioning index, arr[p] is now
            # at right place
            pi = partition(arr,low,high)

            # Separately sort elements before
            # partition and after partition
            quick(arr, low, pi-1)
            quick(arr, pi+1, high)
        return arr

    def merge(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            merge(L)
            merge(R)

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

        return arr

    return locals()[type](arr[:])

if __name__ == '__main__':
    l = [9,2,7,4,5,6,3,8,1]
    print(l)
    print(sort(l, 'quick'))
    print(sort(l, 'merge'))
    print(sort(l, 'insertion'))
