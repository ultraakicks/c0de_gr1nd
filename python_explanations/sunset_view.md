# Compute Buildings with a Sunset View
Given a series of buildings with windows facing West, return the set of buildings that can view the sunset. The input is an array of numbers that represent the height of each building, and the buildings are ordered from [East -> West].

## Examples
```
 Input: [1, 10, 6, 9, 3]
Output: [4, 3, 1]

 Input: [6, 9, 3, 9, 5, 16, 9, 13]
Output: [7, 5]
```

## Solution
```python
def examine_buildings_with_sunset(sequence):
    sunset = []
    curr_max = 0
    for i in reversed(range(len(sequence))):
        if sequence[i] > curr_max:
            curr_max = sequence[i]
            sunset.append(i)
    return sunset
```

## Explanation
* Since the sun sets in the West, and the buildings are ordered from [East -> West], it is easier to process the input sequence from [right -> left]
* The solution iterates over the sequence in reverse, keeps track of the tallest building so far, and if the current building is taller, the index of the current building is pushed to the sunset list

## Code Dissection
1. Create a list to store the indexes of the buildings that can see the sunset and a variable to store the tallest building so far
    ```python
    sunset = []
    curr_max = 0
    ```
2. Loop over the _sequence_ in reverse
    ```python
    for i in reversed(range(len(sequence))):
    ```
3. If the current building is taller than the tallest building so far, set its height as *curr_max* and push the index of the current building to the _sunset_ list
    ```python
    if sequence[i] > curr_max:
        curr_max = sequence[i]
        sunset.append(i)
    ```
4. Return the list of indexes of buildings that can see the sunset
    ```python
    return sunset
    ```