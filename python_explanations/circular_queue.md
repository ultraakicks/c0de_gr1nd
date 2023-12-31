# Implement a Circular Queue
Design a circular queue that supports dynamic resizing.

## Solution
```python
class Queue:

    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.num = 0

    def enqueue(self, x):
        if self.num == len(self.queue):
            self.queue = (self.queue[self.head:] + self.queue[:self.head])
            self.queue += [None] * len(self.queue)
            self.head = 0
            self.tail = self.num
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % len(self.queue)
        self.num += 1

    def dequeue(self):
        if self.num > 0:
            data = self.queue[self.head]
            self.head = (self.head + 1) % len(self.queue)
            self.num -= 1
            return data

    def size(self):
        return self.num
```

## Explanation
* The solution uses a resizable array with a head and tail pointer to implement the circular queue

## Code Dissection - __init__
1. Initialize a list as the queue
    ```python
    self.queue = [None] * capacity
    ```
2. Initialize a head pointer and tail pointer that represent the start and end indices of the queue respectively
    ```python
    self.head = 0
    self.tail = 0
    ```
3. Initialize a variable to store the number of non-empty elements in the queue
    ```python
    self.num = 0
    ```

## Code Dissection - enqueue
1. Check if the queue is full, in which case it needs to be resized
    ```python
    if self.num == len(self.queue):
    ```
    1. Ensure the queue elements will appear in consecutive order
        ```python
        self.queue = (self.queue[self.head:] + self.queue[:self.head])
        ```
    2. Resize the queue by doubling its length
        ```python
        self.queue += [None] * len(self.queue)
        ```
    3. Reset the head and tail pointers
        ```python
        self.head = 0
        self.tail = self.num
        ```
2. Add the element _x_ to the queue
    ```python
    self.queue[self.tail] = x
    ```
3. Increment the tail pointer
    ```python
    self.tail = (self.tail + 1) % len(self.queue)
    ```
4. Increment the number of elements in the queue
    ```python
    self.num += 1
    ```

## Code Dissection - dequeue
1. Check that the queue is not empty
    ```python
    if self.num > 0:
    ```
2. Fetch the data of the element to remove
    ```python
    data = self.queue[self.head]
    ```
3. Increment the head pointer to remove the element from the queue
    ```python
    self.head = (self.head + 1) % len(self.queue)
    ```
    * The queue data is only the data between _head_ and _tail_
4. Decrement the number of elements in the queue
    ```python
    self.num -= 1
    ```
5. Return the data of the dequeued element
    ```python
    return data
    ```

## Code Dissection - size
1. Return the number of elements in the queue
    ```python
    return self.num
    ```