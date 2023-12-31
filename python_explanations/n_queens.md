# Generate All Nonattacking Placements of _n_-Queens
Given _n_ queens on an _n_ &times; _n_ chessboard, compute all nonattacking placements.

Nonattacking placement = no two queens can threaten each other:
1. Queens can't be in same row
2. Queens can't be in same column
3. Queens can't be in same diagonal

## Example
```
 Input: n = 4
Output: [[1, 3, 0, 2], [2, 0, 3, 1]]
```

| A | B |
|---|---|
|<table><tr><td></td><td>&#9819;</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>&#9819;</td></tr><tr><td>&#9819;</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>&#9819;</td><td></td></tr></table>|<table><tr><td></td><td></td><td>&#9819;</td><td></td></tr><tr><td>&#9819;</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>&#9819;</td></tr><tr><td></td><td>&#9819;</td><td></td><td></td></tr></table>|

## Solution
```python
def n_queens(n):
    def dfs(queens, xy_diff, xy_sum):
        row = len(queens)
        if row == n:
            result.append(queens)
        for col in range(n):
            if col not in queens and row - col not in xy_diff and row + col not in xy_sum:
                dfs(queens + [col], xy_diff + [row - col], xy_sum + [row + col])
    result = []
    dfs([], [], [])
    return result
```

## Explanation
* For any point (_x_, _y_), if the new point (_p_, _q_) shouldn't share the same row, column, or diagonal, then we must have:
    1. _p_ + _q_ != _x_ + _y_: eliminate left bottom right top diagonal
    2. _p_ - _q_ != _x_ - _y_: eliminate left top right bottom diagonal

## Code Dissection - dfs
1. Set the row as the length of _queens_, which is the list of column index per row
    ```python
    row = len(queens)
    ```
2. If the current row is equal to _n_, then add it to _queens_
    ```python
    if row == n:
        result.append(queens)
    ```
3. For any point (_x_, _y_), find a new point (_p_, _q_) that does not share the same row, column, or diagonal
    ```python
    for col in range(n):
        if col not in queens and row - col not in xy_diff and row + col not in xy_sum:
            dfs(queens + [col], xy_diff + [row - col], xy_sum + [row + col])
    ```
    * `queens` the list of column index per row
    * `row` the current row where we're searching for a valid column
    * `xy_diff` the list of _x_ - _y_
    * `xy_sum` the list of _x_ + _y_

## Code Dissection - n_queens
1. Create a list to hold the result, run `dfs()` with empty lists as the input, then return the result
    ```python
    result = []
    dfs([], [], [])
    return result
    ```