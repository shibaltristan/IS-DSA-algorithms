from typing import List, Callable, Optional, Any

# Simple implementations of sorting/searching to demonstrate algorithms

def bubble_sort(items: List[Any], key: Callable[[Any], Any] = lambda x: x, reverse: bool = False) -> List[Any]:
    arr = items[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (key(arr[j]) < key(arr[j + 1])) if reverse else (key(arr[j]) > key(arr[j + 1])):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(items: List[Any], key: Callable[[Any], Any] = lambda x: x, reverse: bool = False) -> List[Any]:
    if len(items) <= 1:
        return items[:]
    pivot = key(items[len(items) // 2])
    left = [x for x in items if (key(x) > pivot) if reverse else (key(x) < pivot)]
    middle = [x for x in items if key(x) == pivot]
    right = [x for x in items if (key(x) < pivot) if reverse else (key(x) > pivot)]
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)


def binary_search_by_key(sorted_items: List[Any], target, key: Callable[[Any], Any]) -> Optional[int]:
    """Binary search on sorted_items. Returns index or None. Assumes sorted_items is sorted ascending by key."""
    lo = 0
    hi = len(sorted_items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_val = key(sorted_items[mid])
        if mid_val == target:
            return mid
        elif mid_val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return None
