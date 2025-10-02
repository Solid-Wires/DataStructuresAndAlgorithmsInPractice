
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
        # Get out of the loop if we didn't swap at all
        if swapped == False:
            break

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

# Sort an array using merge sort
# O(nlog(n)) complexity
# https://www.geeksforgeeks.org/dsa/merge-sort/
# GeeksForGeeks' implementation is a little strange. This implementation is going to
# be a lot more compact and gets straight to the point for the initial left and right values.
def merge_sort(arr0: list[int]):
    
    # Merge two lists.
    def merge(arr1: list[int], left: int, mid: int, right:int):
        pass
    
    left: int = 0
    right: int = len(arr0) - 1
    
    raise NotImplementedError
