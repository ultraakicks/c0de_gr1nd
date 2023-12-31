# Search a Sorted Array for First Occurrence of _k_
Given a sorted array _A_ and an integer _k_, return the index of the first occurrence of _k_. Return -1 if _k_ isn't in the array.

## Examples
```
 Input: k = 4
        [0, 1, 2, 3, 4, 5, 6, 7]
Output: 4

 Input: k = 2
        [0, 0, 0, 1, 1, 1, 1, 1, 2]
Output: 8
```

## Solution
```python
def search_first_of_k(A, k):
    left = 0
    right = len(A) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] < k:
            left = mid + 1
        elif A[mid] > k:
            right = mid - 1
        else:
            result = mid
            right = mid - 1
    return result
```

## Explanation
* The solution is a slightly modified binary search

## Code Dissection
1. Create a left and right pointer at the start and end of the array respectively
    ```python
    left = 0
    right = len(A) - 1
    ```
2. Initialize a variable to store the result at -1, because -1 is the default case that _k_ is not in _A_
    ```python
    result = -1
    ```
3. Loop until the left and right pointer pass each other
    ```python
    while left <= right:
    ```
4. Compute the mid pointer
    ```python
    mid = (left + right) // 2
    ```
5. Check if _k_ is at _mid_
    ```python
    if A[mid] < k:
        left = mid + 1
    elif A[mid] > k:
        right = mid - 1
    else:
        result = mid
        right = mid - 1
    ```
    * Keep in mind that even if _k_ is found, that does not mean it is the first occurrence of _k_
6. Return the first occurrence of _k_
    ```python
    return result
    ```