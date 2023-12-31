# Compute the Successor
Given a node in a binary tree, return its successor. The successor is the next node in an inorder traversal.

## Example
```
        1
       / \
      2   3
     / \
    7   5

Inorder Traversal: [7, 2, 5, 1, 3]

 Input: node = 2
Output: 5
```

## Solution
```python
def find_successor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    while node.parent and node.parent.right is node:
        node = node.parent
    return node.parent
```

## Explanation
* If the right subtree exists, the successor is the leftmost node in the right subtree
* If the right subtree does not exist, the successor is the closest ancestor whose left subtree contains the given node
* If there is no successor, then the given node is the rightmost node in the tree

## Code Dissection
1. If the right subtree exists, find the leftmost node in the right subtree and return that as the successor
    ```python
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    ```
2. If the right subtree does not exist, find the parent whose left subtree contains the given node and return that as the sucessor
    ```python
    while node.parent and node.parent.right is node:
        node = node.parent
    return node.parent
    ```