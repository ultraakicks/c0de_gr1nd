# Compute the _k_ Closest Stars
Given a 2D array, where each element is an array of coordinates, compute the _k_ closest stars to Earth, which is located at (0, 0, 0).

## Example
```
 Input: k = 2
        [
     [-1794.8070372385318, -9120.626275560508, -2021.3955677174254],
     [6945.623209746882, 8283.632617219755, 9623.435301592799],
     [9263.718591572451, 656.5773156171654, -1503.123327920437],
     [6670.133011049249, 2279.2320407562183, -4073.4724736107464],
     [-5026.933414485983, 4445.885340427358, -1120.6910284437745],
     [2210.0812228916748, 595.7866615882303, -5213.652239247229],
     [6575.568191268754, 672.3147857301883, 6332.234818341198],
     [-3684.2924115999813, -3833.0027029766643, -248.96523550172606]
 ]
Output: [5322.396451194523, 5693.995998392733]
```

## Solution
```python
def find_closest_k_stars(stars, k):
    max_heap = []
    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return [star[1] for star in heapq.nlargest(k, max_heap)]
```

## Explanation
1. Add the first _k_ stars to the max-heap
2. Add each new star to the max-heap and extract the maximum
3. Extract the _k_ largest stars from the max-heap
* Make sure the max-heap is sorted by the star's distance

## Code Dissection
1. Create a max-heap
    ```python
    max_heap = []
    ```
2. Iterate through every star and process them through the max-heap
    ```python
    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    ```
    1. Add the first _k_ stars to the max-heap
    2. Add each new star to the max-heap and extract the maximum
    * `-star.distance` is used, because `heapq` does not implement a max-heap
3. Extract the _k_ largest stars from the max-heap
    ```python
    return [star[1] for star in heapq.nlargest(k, max_heap)]
    ```