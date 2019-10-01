# Convert from Roman to Decimal 
The Roman numeral representation of positive integers uses the symbols _I_, _V_, _X_, _L_, _C_, _D_, _M_. Each symbol represents a value, with _I_ being 1, _V_ being 5, _X_ being 10, _L_ being 50, _C_ being 100, _D_ being 500, and _M_ being 1000.  
  
In this problem we give simplified rules for representing numbers in this system. Specifically, we define a string over the Roman number symbols to be a valid Roman number string if symbols appear in nonincreasing order, with the following exceptions allowed:

* _I_ can immediately precede _V_ and _X_.
* _X_ can immediately precede _L_ and _C_.
* _C_ can immediately precede _D_ and _M_.

Back-to-back exceptions are not allowed, e.g., _IXC_ is invalid, as is _CDM_.  
  
A valid complex Roman number string represents the integer which is the sum of the symbols that do not correspond to exceptions; for the exceptions, add the difference of the larger symbol and the smaller symbol.  
  
For example, the strings "XXXXXIIIIIIIII", "LVIIII", and "LIX" are valid Roman number strings representing 59. The shortest valid complex Roman number string corresponding to the integer 59 is "LIX".  
  
Write a program which takes as input a valid Roman number string _s_ and returns the integer it corresponds to.

  
## Examples
```
 Input: 'LIX'
Output: 59

 Input: 'XVII'
Output: 17

 Input: 'XLVII'
Output: 47
```
  
## Solution
```python
def roman_to_integer(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev = 0
    for char in s[::-1]:
        if roman[char] < prev:
            result -= roman[char]
        else:
            result += roman[char]
        prev = roman[char]
    return result
```
  
## Explanation
* The solution iterates over the Roman numerals from right -> left and follows 2 simple rules:
    1. When a symbol appears after a larger symbol, it is subtracted
    2. When a symbol appears before a larger symbol, it is added
  
## Code Dissection
1. Create a dictionary that maps the Roman numerals to their corresponding decimal values
    ```python
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ```
2. Create variables to hold the result and the previous symbol's value
    ```python
    result = 0
    prev = 0
    ```
3. Loop over each symbol in the string from right -> left
    ```python
    for char in s[::-1]:
    ```
    a. Implement Rule #1 - When a symbol appears after a larger symbol, it is subtracted
    ```python
    if roman[char] < prev:
        result -= roman[char]
    ```
    b. Implement Rule #2 - When a symbol appears before a larger symbol, it is added
    ```python
    else:
        result += roman[char]
    ```
    c. Set the previous symbol to the current symbol for the next loop iteration
    ```python
    prev = roman[char]
    ```
4. Return the computed integer
    ```python
    return result
    ```