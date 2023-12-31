# Find the Closest Entries in Three Sorted Arrays
Given three sorted arrays, compute a value from each array that forms the smallest possible interval.

## Example
```
 Input: [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
 ]
Output: 4
Minimum interval = [3, 4, 7]
Minimum distance = 7 - 3 = 4
```

## Solution
```python
def find_closest_elements_in_sorted_arrays(sorted_arrays):
    diff = float('inf')
    tree = SortedDict()
    for idx, array in enumerate(sorted_arrays):
        i = iter(array)
        nxt = next(i)
        tree[(nxt, idx)] = i
    while True:
        min_val, min_idx = tree.peekitem(0)[0]
        max_val = tree.peekitem()[0][0]
        diff = min(diff, max_val - min_val)
        i = tree.popitem(0)[1]
        nxt = next(i, None)
        if nxt is None:
            return diff
        tree[(nxt, min_idx)] = i
```

## Explanation
Let _s_ be the minimum value and _b_ be the maximum value in a set of 3 numbers:
1. Get the first element from each sorted array
2. Remove _s_ from the set and replace it with the next element in the array that it belongs to
3. The current distance is (_b_ - _s_)
4. Keep comparing the current distance with the smallest distance so far
5. Return the smallest distance

## Code Dissection
1. Initialize the current distance (difference between the smallest and largest) to infinity, so that the initial minimum distance calculated will always be smaller
    ```python
    diff = float('inf')
    ```
2. Use a BST to help keep track of the minimum value, maximum value, and iterators
    ```python
    tree = SortedDict()
    ```
    * A `SortedDict` from `sortedcontainers` is a highly optimized data structure that can act like a BST
3. For our initial set of 3 elements, put the first element from each array in the tree, along with its index
    ```python
    i = iter(array)
    nxt = next(i)
    tree[(nxt, idx)] = i
    ```
    * Rather than using an iterator variable, creating an iterator object for each array makes it easy to get the next array element when needed
4. Loop until we hit the end of one of the arrays
    ```python
    while True:
    ```
5. Get the current minimum value and maximum value in the tree
    ```python
    min_val, min_idx = tree.peekitem(0)[0]
    max_val = tree.peekitem()[0][0]
    ```
6. Calculate the current difference, then compare it to the smallest difference so far
    ```python
    diff = min(diff, max_val - min_val)
    ```
7. Remove the smallest value from the tree, then get the next element in the array that it belonged to
    ```python
    i = tree.popitem(0)[1]
    nxt = next(i, None)
    ```
8. If we reach the end of an array, return the smallest difference computed
    ```python
    if nxt is None:
        return diff
    ```
9. Otherwise, put the next element from the array in the tree
    ```python
    tree[(nxt, min_idx)] = i
    ```