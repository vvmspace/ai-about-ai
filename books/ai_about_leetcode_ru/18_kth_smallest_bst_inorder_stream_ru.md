# 18. Kth Smallest Element in a BST: inorder как отсортированный поток

У BST есть золотое свойство: inorder-обход выдаёт значения по возрастанию. Значит, `k`-й элемент — это просто `k`-й шаг в этом потоке.

Сложность:
- время: **O(h + k)** в среднем;
- память: **O(h)** на стек обхода.

Термины: **inorder stream**, **rank query**, **early stop**.

```python
def kthSmallest(root, k):
    stack = []
    cur = root

    while True:
        while cur:
            stack.append(cur)  # Идём максимально влево.
            cur = cur.left

        cur = stack.pop()      # Следующий элемент в отсортированном порядке.
        k -= 1
        if k == 0:
            return cur.val      # Ранний выход на нужном ранге.

        cur = cur.right
```

> “I consume nodes as an inorder sorted stream and stop exactly at rank k without traversing the whole tree.”

- [Kth Smallest Element in a BST на LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [Оглавление книги](./README.md)
