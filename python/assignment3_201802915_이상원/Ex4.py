# Merge Sort


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        l, r, idx = 0, 0, 0
        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                arr[idx] = L[l]
                l += 1
                idx += 1
            else:
                arr[idx] = R[r]
                r += 1
                idx += 1
        while l < len(L):
            arr[idx] = L[l]
            l += 1
            idx += 1
        while r < len(R):
            arr[idx] = R[r]
            r += 1
            idx += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [5, 3, 1, 4, 7, 0]
    print("Input Array:")
    printList(arr)
    mergeSort(arr)
    print("Sorted Array:")
    printList(arr)
