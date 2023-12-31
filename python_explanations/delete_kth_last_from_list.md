# Remove the *k*th Last Element from a List
Given a singly linked list and an integer _k_, remove the *k*th last element from the list.

## Example
```
k = 2

 Input: L -> [1] -> [2] -> [3] -> [4] -> [5] -> None
Output: L -> [1] -> [2] -> [3] -> [5] -> None
```

## Solution
```python
def remove_kth_last(L, k):
    slow = fast = L
    for _ in range(k):
        fast = fast.next
    if not fast:
        return L.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return L
```

## Explanation
* The solution uses two pointers to traverse the list:
    1. First, the fast pointer moves _k_ steps
    2. Then, the slow pointer and the fast pointer move one step at a time until the fast pointer reaches the tail of the list
* When the _fast_ pointer is at the tail of the list, the _slow_ pointer is at the (_k_ + 1)th last node
* If the fast pointer is at the tail of the list before iterating the slow pointer, then it is the head node that needs to be removed

## Code Dissection
1. Initialize a slow pointer and fast pointer to the head of _L_
    ```python
    slow = fast = L
    ```
2. Move the fast pointer _k_ steps
    ```python
    for _ in range(k):
        fast = fast.next
    ```
3. If the fast pointer is at the tail, remove the head
    ```python
    if not fast:
        return L.next
    ```
4. Move the slow and fast pointer until the fast pointer reaches the tail
    ```python
    while fast.next:
        fast = fast.next
        slow = slow.next
    ```
5. Remove the *k*th node from the end of the list
    ```python
    slow.next = slow.next.next
    ```
6. Return the head of the list
    ```python
    return L
    ```