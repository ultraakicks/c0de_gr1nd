# Check if a Decimal Integer is a Palindrome
Given an integer _x_, determine whether or not its decimal representation is palindromic.

## Examples
```
0    -> True
11   -> True
215  -> False
-1   -> False
777  -> True
```

## Solution
```python
def is_palindrome_number(x):
    if x < 0:
        return False
    reverse = 0
    tmp = x
    while tmp:
        reverse = reverse * 10 + tmp % 10
        tmp //= 10
    return x == reverse
```

## Pythonic Solution
```python
def is_palindrome_number_pythonic(x):
    return False if x < 0 else x == int(str(x)[::-1])
```

## Explanation
* The solution uses some relatively simple arithmetic to perform 3 key steps to build the reversed number:
    1. Extract the last digit in the number
    2. Append the extracted digit to the reversed number
    3. Remove the last digit from the number
* After the reversed number is computed, it is compared to the original number to check if it is palindromic
    * If the reversed number is equal to the original number, then the number is a palindrome

## Code Dissection
1. Check the sign of the number, because negative numbers cannot be palindromic
    ```python
    if x < 0:
        return False
    ```
2. Initialize variables to hold the reversed number and a copy of the original number
    ```python
    reverse = 0
    tmp = x
    ```
3. Loop until the temporary variable is empty, which happens when the reversed number has been computed
    ```python
    while tmp:
    ```
    * `while tmp` is equivalent to `while tmp == 0` in this case, because _tmp_ will always equal zero by the end of this operation
4. Extract the last digit from _tmp_ and append it to the reversed number
    ```python
    reverse = reverse * 10 + tmp % 10
    ```
5. Remove the last digit from _tmp_
    ```python
    tmp //= 10
    ```
6. Check for palindromicity by comparing the reversed number to the original number
    ```python
    return x == reverse
    ```

## Pythonic Code Dissection
1. Use built-in functions to convert the number to a string, use slice notation to reverse the number string, convert the reversed number string back to an integer, then compare the reversed number to the original number to test for palindromicity
    ```python
    return False if x < 0 else x == int(str(x)[::-1])
    ```
    Let's separate this concise one-liner into multiple lines for easier readability:
    ```python
    if x < 0:
        return False
    else:
        return x == int(str(x)[::-1])
    ```
    * Now we can clearly see there are two cases: 1 for negative numbers and 1 for positive numbers
    * Negative numbers cannot be palindromic, so we return False
    * `abs(x)` returns the absolute value of _x_
    * `str(x)[::-1]` converts _x_ into a string and reverses it using slice notation
    * `int(str(x))` converts the reversed string back into an integer