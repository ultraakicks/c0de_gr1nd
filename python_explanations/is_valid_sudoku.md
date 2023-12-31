# The Sudoku Checker Problem
Check whether or not a 9 &times; 9 2D array contains valid sudoku numbers. 0's in the array represent blank spots.

## Examples
```
Input: [[0, 7, 0, 0, 0, 0, 1, 3, 0],
        [0, 0, 0, 9, 2, 7, 0, 6, 0],
        [4, 0, 0, 0, 0, 0, 0, 8, 9],
        [3, 0, 1, 0, 5, 0, 6, 4, 0],
        [0, 0, 8, 4, 0, 9, 2, 0, 0],
        [0, 0, 7, 1, 6, 0, 5, 0, 0],
        [0, 2, 0, 0, 9, 1, 0, 0, 7],
        [0, 0, 5, 8, 0, 0, 0, 0, 0],
        [6, 3, 0, 2, 0, 0, 0, 0, 4]]
Output:	True

Input: [[0, 7, 0, 0, 0, 0, 8, 0, 0],
        [6, 0, 0, 0, 1, 0, 0, 0, 5],
        [3, 0, 0, 0, 6, 0, 0, 0, 4],
        [0, 5, 0, 0, 0, 0, 7, 6, 0],
        [0, 1, 2, 1, 0, 0, 0, 0, 0],
        [9, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 1],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
Output: False
```

## Solution
```python
def is_valid_list(section):
    section = [x for x in section if x != 0]
    return len(section) == len(set(section))


def is_valid_sudoku(grid):
    for i in range(9):
        if not is_valid_list(grid[i]) or not is_valid_list([col[i] for col in grid]):
            return False
    for i in range(3):
        for j in range(3):
            if not is_valid_list(
                grid[a][b]
                for a in range(j * 3, 3 * (j + 1))
                for b in range(i * 3, 3 * (i + 1))
            ):
                return False
    return True
```

## Explanation
Let's look at the layout of a sudoku board:
```
1 1 1 | 2 2 2 | 3 3 3
1 1 1 | 2 2 2 | 3 3 3
1 1 1 | 2 2 2 | 3 3 3
---------------------
4 4 4 | 5 5 5 | 6 6 6
4 4 4 | 5 5 5 | 6 6 6
4 4 4 | 5 5 5 | 6 6 6
---------------------
7 7 7 | 8 8 8 | 9 9 9
7 7 7 | 8 8 8 | 9 9 9
7 7 7 | 8 8 8 | 9 9 9
```
* The board has been filled with numbers that represent their sub-grid number
* The main challenge of the problem is finding out how to grab each column, row, and sub-grid
* Let's look at extracting each row, column, and sub-grid by hand:
    ```python
    row1 = grid[0]
    row2 = grid[1]
    row3 = grid[2]
    row4 = grid[3]
    row5 = grid[4]
    row6 = grid[5]
    row7 = grid[6]
    row8 = grid[7]
    row9 = grid[8]

    col1 = [col[0] for col in grid]
    col2 = [col[1] for col in grid]
    col3 = [col[2] for col in grid]
    col4 = [col[3] for col in grid]
    col5 = [col[4] for col in grid]
    col6 = [col[5] for col in grid]
    col7 = [col[6] for col in grid]
    col8 = [col[7] for col in grid]
    col9 = [col[8] for col in grid]

    subgrid1 = [grid[a][b] for a in range(0, 3) for b in range(0, 3)]
    subgrid2 = [grid[a][b] for a in range(0, 3) for b in range(3, 6)]
    subgrid3 = [grid[a][b] for a in range(0, 3) for b in range(6, 9)]
    subgrid4 = [grid[a][b] for a in range(3, 6) for b in range(0, 3)]
    subgrid5 = [grid[a][b] for a in range(3, 6) for b in range(3, 6)]
    subgrid6 = [grid[a][b] for a in range(3, 6) for b in range(6, 9)]
    subgrid7 = [grid[a][b] for a in range(6, 9) for b in range(0, 3)]
    subgrid8 = [grid[a][b] for a in range(6, 9) for b in range(3, 6)]
    subgrid9 = [grid[a][b] for a in range(6, 9) for b in range(6, 9)]
    ```
* When everything is written out by hand, it is a lot easier to compose a generator expression and understand the code in the solution:
    ```python
    rows = [grid[i] for i in range(9)]
    cols = [[col[i] for col in grid] for i in range(9)]
    subgrids = (
            [grid[a][b]
                for a in range(j * 3, 3 * (j + 1))
                for b in range(i * 3, 3 * (i + 1))
        ]   for i in range(3) for j in range(3)
    )
    ```

## Code Dissection - is_valid_list
1. Filter out the zeroes from the list &mdash; they represent blank entries
    ```python
    section = [x for x in section if x != 0]
    ```
2. Return whether or not the filtered list contains any duplicates
    ```python
    return len(section) == len(set(section))
    ```
    * `len(set(x))` tells us the size of unique elements in x
    * This statement is comparing the size of the filtered list to the size of unique elements &mdash; if they are not equal, then the list contains duplicates

## Code Dissection - is_valid_sudoku
1. Loop over each column and grid to check for duplicates
    ```python
    for i in range(9):
        if not is_valid_list(grid[i]) or not is_valid_list([col[i] for col in grid]):
            return False
    ```
2. Loop over each sub-grid and check for duplicates
    ```python
    for i in range(3):
        for j in range(3):
            if not is_valid_list(
                grid[a][b]
                for a in range(j * 3, 3 * (j + 1))
                for b in range(i * 3, 3 * (i + 1))
            ):
                return False
    ```
3. If there are no duplicates in each row, column, and sub-grid, then the sudoku grid is valid
    ```python
    return True
    ```