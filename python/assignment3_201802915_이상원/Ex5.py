# Quick Sort

# This function takes last element as pivot
def partition(arr, low, high):
    i = low  # Index of smaller element
    pivot = arr[low]  # Pivot
    pi = high

    fin = False
    while not fin:
        while i <= pi and arr[i] <= pivot:
            i += 1
        while i <= pi and pivot <= arr[pi]:
            pi -= 1
        if pi < i:
            fin = True
        else:
            arr[i], arr[pi] = arr[pi], arr[i]
    arr[low], arr[pi] = arr[pi], arr[low]

    return pi


# The main function that implements QuickSort
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place 
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition 
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [5, 3, 1, 4, 7, 0]
    print("Input Array:")
    printList(arr)
    quickSort(arr, 0, len(arr) - 1)
    print("Sorted Array:")
    printList(arr)
