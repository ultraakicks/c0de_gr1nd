# Compute a Random Permutation
Given a random number generator that returns integers in the set [0, 1, ... , _n_-1], compute a random permutation of that set with equal probability.

## Examples
```
n = 5
Output1: [1, 3, 2, 0, 4]
Output2: [0, 4, 2, 3, 1]
Output3: [3, 2, 0, 1, 4]

n = 7
Output1: [0, 4, 2, 5, 1, 6, 3]
Output2: [3, 1, 5, 4, 2, 6, 0]
Output3: [4, 5, 1, 3, 2, 6, 0]
```

## Solution
```python
def compute_random_permutation(n):
    perm = list(range(n))
    perm[:] = random.sample(perm, n)
    return perm
```

## Explanation
* Despite what the problem description states, you are not given a random number generator; it is referring to the solution from [Sample Offline Data](offline_sampling.md)
* Create a list from [0, ... , _n_-1], then create a permutation of that list

## Code Dissection
1. Create a list filled with the numbers [0, ... , _n_-1]
    ```python
    perm = list(range(n))
    ```
2. Use `random.sample(population, k)` to create a permutation of perm
    ```python
    perm[:] = random.sample(perm, n)
    ```
3. Return the uniformly random permutation
    ```python
    return perm
    ```