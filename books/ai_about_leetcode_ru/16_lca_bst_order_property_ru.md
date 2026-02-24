# 16. Lowest Common Ancestor of BST: использовать порядок, а не силу

Здесь многие делают полный обход дерева. Это работает, но выглядит расточительно, потому что BST уже дал вам структурное преимущество.

Если оба значения меньше текущего узла — идём влево.
Если оба больше — идём вправо.
Иначе текущий узел и есть LCA.

Сложность:
- время: **O(h)**;
- память: **O(1)** в итеративной версии.

Неочевидные термины:
- **ordering invariant** — инвариант BST: слева меньше, справа больше;
- **split point** — узел, где пути к `p` и `q` расходятся;
- **path convergence** — точка сходимости двух поисковых путей.

Пример на JavaScript:

```javascript
function lowestCommonAncestor(root, p, q) {
  let node = root;

  while (node) {
    if (p.val < node.val && q.val < node.val) {
      node = node.left;
    } else if (p.val > node.val && q.val > node.val) {
      node = node.right;
    } else {
      return node;
    }
  }

  return null;
}
```

Интервью-ответ:

> “In a BST, I do not need to explore both subtrees blindly. I walk down using ordering: left if both targets are smaller, right if both are larger. The first split point is the LCA.”  
> [«В BST мне не нужно вслепую исследовать оба поддерева. Я спускаюсь по порядку: влево, если обе цели меньше, вправо, если обе больше. Первая точка расхождения и есть LCA».]

Пара фраз:
- “Use structure before brute force.”  
  [«Сначала используй структуру, потом силу».]
- “The split point answers the question.”  
  [«Точка расхождения даёт ответ».]

Где это в работе: поиск общего уровня прав доступа, определение общего родителя категорий, навигация по иерархиям конфигураций.

Полезные ссылки:
- [Lowest Common Ancestor of a Binary Search Tree на LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [Оглавление книги](./README.md)
