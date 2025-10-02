
# Sort an array using the infamous, naive bubble sort
# O(n^2) complexity
# https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/
def bubble_sort(arr: list[int]):
    n: int = len(arr)
    
    # Start from index 0 to size of list exclusive (n - 1)
    for i in range(n):
        swapped: bool = False
        
        # Last i elements are already in place
        # Traverse the array from 0 to last i elements exclusive (n - i - 2)
        for j in range(0, n - i - 1):
            
            # Swap if this element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # # Get out of the loop if we didn't swap at all
        # # NOTE: This is GeeksForGeeks' optimization of bubble sort.
        # # Commented out to display terrible performance complexity
        # # But the algorithm shows significant improvement with this condition,
        # # almost equivalent to linear sort because it reduces its complexity to about O(n)
        # if swapped == False:
        #     break

# Sort an array using insertion sort
# O(n) complexity
# https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/
def insertion_sort(arr: list[int]):
    n: int = len(arr)
    
    # Start from index 1 to size of list exclusive (n - 1)
    for i in range(1, n):
        cur: int = arr[i]
        j: int = i - 1
        
        # previous (j) must be greater than 0 and current must be less than the previous integer
        # If so, then we move this smaller integer backwards until it's in the right placement
        # e.g. [8, 12, 11] becomes [8, 11, 12] on last passthrough
        while j >= 0 and cur < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur

# Merge two lists (helper for merge sort)
def merge(arr: list[int], left: int, mid: int, right: int):
    n0: int = mid - left + 1
    n1: int = right - mid
    
    # Create temp arrays, initialized to 0
    L: list[int] = [0] * n0
    R: list[int] = [0] * n1
    
    # Copy data to temo arrays L[] and R[]
    for i in range(n0):
        L[i] = arr[left + i]
    for j in range(n1):
        R[j] = arr[mid + 1 + j]
    
    i: int = 0
    j: int = 0
    k: int = left
    
    # Merge the temp arrays back
    # into arr[left..right]
    while i < n0 and j < n1:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy the remaining eleents of L[],
    # if there are any
    while i < n0:
        arr[k] = L[i]
        i += 1
        k += 1
    # Copy the remaining eleents of R[],
    # if there are any
    while j < n1:
        arr[k] = R[j]
        j += 1
        k += 1

# Sort an array using merge sort
# O(nlog(n)) complexity
# https://www.geeksforgeeks.org/dsa/merge-sort/
def merge_sort(arr0: list[int], left: int = 0, right: int = -1):
    if right < 0: right = len(arr0) - 1
    if left < right:
        mid = (left + right) // 2
        
        merge_sort(arr0, left, mid)
        merge_sort(arr0, mid + 1, right)
        merge(arr0, left, mid, right)
