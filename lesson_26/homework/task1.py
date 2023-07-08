def bBubbleSort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Pass moving up
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        # Pass moving down
        end -= 1
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        start += 1

    return arr

arr = [1, 5, 3, 2, 4, 7, 6, 10, 9, 8]
print(arr)
print(bBubbleSort(arr))