# 18. Kth Smallest Element in a BST: inorder как отсортированный поток

Для BST inorder-обход выдаёт значения по возрастанию. Значит, достаточно пройти дерево и остановиться на `k`-м элементе.

Сложность:
- время: **O(h + k)** в среднем;
- память: **O(h)** на стек.

Термины: **inorder stream**, **early stopping**, **rank query**.

```python
def kthSmallest(root, k):
    stack = []
    cur = root

    while True:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val

        cur = cur.right
```

> “I consume BST nodes as an inorder stream and stop exactly at rank k, avoiding full traversal.”

- [Kth Smallest Element in a BST на LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [Оглавление книги](./README.md)
