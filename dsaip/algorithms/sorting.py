
# Sort an array using the infamous, naive bubble sort
# O(n^2) complexity
def bubble_sort(list: list[int]):
    raise NotImplementedError

# Sort an array using insertion sort
# O(n) complexity
# https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/
def insertion_sort(list: list[int]):
    
    # Start from index 1 to end of list (n - 1)
    for idx in range(1, len(list)):
        cur: int = list[idx]
        prev = idx - 1
        
        # previous must be greater than 0 and current must be less than the previous integer
        # If so, then we move this smaller integer backwards until it's in the right placement
        # e.g. [8, 12, 11] becomes [8, 11, 12] on last passthrough
        while prev >= 0 and cur < list[prev]:
            list[prev + 1] = list[prev]
            prev -= 1
        list[prev + 1] = cur

# Sort an array using merge sort
# O(nlog(n)) complexity
def merge_sort(list: list[int]):
    raise NotImplementedError
