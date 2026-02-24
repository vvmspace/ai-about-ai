# 16. Lowest Common Ancestor of BST: сила упорядоченности

В BST порядок даёт короткий путь: если оба узла меньше текущего — идём влево; если больше — вправо; иначе это LCA.

Сложность:
- время: **O(h)**;
- память: **O(1)** для итеративной версии.

Термины: **order property**, **split point**, **ancestor dominance**.

```python
def lowestCommonAncestor(root, p, q):
    cur = root
    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur
```

> “I leverage BST ordering to find the split point where paths to p and q diverge; that node is the LCA.”

- [Lowest Common Ancestor of BST на LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [Оглавление книги](./README.md)
