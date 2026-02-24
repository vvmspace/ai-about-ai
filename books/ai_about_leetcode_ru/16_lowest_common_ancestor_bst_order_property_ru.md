# 16. Lowest Common Ancestor of BST: сила упорядоченности

В обычном бинарном дереве LCA требует полного анализа пути. В **BST** порядок снимает половину работы. Если оба узла меньше текущего — идём влево. Если оба больше — вправо. В точке расхождения и находится ответ.

Сложность:
- время: **O(h)**;
- память: **O(1)** для итеративной версии.

Термины: **split point**, **order property**, **path divergence**.

```python
def lowestCommonAncestor(root, p, q):
    cur = root

    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left   # Оба узла в левом поддереве.
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right  # Оба узла в правом поддереве.
        else:
            return cur       # Точка расхождения путей.
```

> “I leverage BST ordering to find the first split point between paths to p and q; that node is the LCA.”

- [Lowest Common Ancestor of BST на LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [Оглавление книги](./README.md)
