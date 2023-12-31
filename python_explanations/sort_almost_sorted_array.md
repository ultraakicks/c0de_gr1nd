# Sort an Almost-Sorted Array
Given an array of numbers, where each element is at most _k_ away from its sorted position, sort the array.

## Examples
```
 Input: k = 4
        [1, 2, 0, 3]
Output: [0, 1, 2, 3]

 Input: k = 5
        [-5, -3, -2, -5, 3]
Output: [-5, -5, -3, -2, 3]
```

## Solution
```python
def sort_approximately_sorted_array(sequence, k):
    min_heap = []
    result = []
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)
    for x in sequence:
        result.append(heapq.heappushpop(min_heap, x))
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result
```

## Explanation
* Note that the input is an iterator object and not a list
1. Add the first _k_ elements to the min-heap (stop if fewer than _k_)
2. Add each new element in the sequence to the min-heap and extract the smallest
3. After the sequence is exhausted, extract the remaining elements from the min-heap

## Code Dissection
1. Create a min-heap and a list to store the result
    ```python
    min_heap = []
    result = []
    ```
2. Add the first _k_ elements to the min-heap, stopping if there are less than _k_ elements in _sequence_
    ```python
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)
    ```
3. Add each new element in _sequence_ to the min-heap and extract the smallest element
    ```python
    for x in sequence:
        result.append(heapq.heappushpop(min_heap, x))
    ```
4. After the sequence is exhausted, extract the remaining elements from the *min_heap* and append them to _result_
    ```python
    while min_heap:
        result.append(heapq.heappop(min_heap))
    ```
5. Return the sorted list
    ```python
    return result
    ```