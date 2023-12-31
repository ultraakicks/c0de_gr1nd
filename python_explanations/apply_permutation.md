# Permute the Elements of an Array
Given an array _A_, reorder the elements to the permutation given in the index array _P_.

## Examples
```
A = [5, 0, 2, 1, 4, 3]
P = [3, 0, 5, 4, 2, 1]
Output: [0, 3, 4, 5, 1, 2]

A = [4, 5, 0, 3, 2, 1]
P = [5, 4, 3, 1, 2, 0]
Output: [1, 3, 2, 0, 5, 4]
```

## Solution
```python
def apply_permutation(perm, A):
    B = [0] * len(A)
    for i in range(len(A)):
        B[perm[i]] = A[i]
    A[:] = B
```

## Explanation
* Create an array _B_ to hold the desired sequence, fill it, then make _A_ = _B_

## Code Dissection
1. Create an array _B_ to store the desired sequence from the permutation
    ```python
    B = [0] * len(A)
    ```
2. Iterate through _A_, get the value at _A_[_i_], and put it in _B_ at the index of perm[_i_]
    ```python
    for i in range(len(A)):
        B[perm[i]] = A[i]
    ```
3. Set _A_ = _B_, since _B_ now holds the desired permutation
    ```python
    A[:] = B
    ```
    * The difference between `A[:] = B` and `A = B` is that the latter will not replace elements in the original list _A_