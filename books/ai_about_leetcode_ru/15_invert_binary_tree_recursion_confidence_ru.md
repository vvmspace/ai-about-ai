# 15. Invert Binary Tree: рекурсия без лишней драмы

Эта задача проверяет зрелость базовой работы с деревом. Не скорость печати. Не хитрость. Чистую модель обхода.

Суть: для каждого узла меняем местами левого и правого ребёнка, затем повторяем то же для поддеревьев.

Можно делать рекурсией или итеративно через очередь. На интервью рекурсия обычно читается чище.

Сложность:
- время: **O(n)**;
- память: **O(h)** для рекурсии, где `h` — высота дерева.

Неочевидные термины:
- **tree symmetry transform** — преобразование структуры, сохраняющее набор значений;
- **post-swap traversal** — обход после локального обмена детей;
- **call stack depth** — глубина стека вызовов, критичная для вырожденного дерева.

Пример на Python:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root
```

Интервью-ответ:

> “I apply a local swap at each node and recurse into both children. Every node is processed exactly once, so time is linear, while extra space is proportional to tree height due to recursion depth.”  
> [«Я применяю локальный обмен детей в каждом узле и рекурсивно иду в оба поддерева. Каждый узел обрабатывается ровно один раз, поэтому время линейное, а дополнительная память пропорциональна высоте дерева из-за глубины рекурсии».]

Пара фраз:
- “Simple transform, strict traversal.”  
  [«Простая трансформация, строгий обход».]
- “Trees reward calm recursion.”  
  [«Деревья вознаграждают спокойную рекурсию».]

Где это в работе: зеркалирование и нормализация иерархий меню, преобразование AST в компиляторах, симметричные операции над деревом разрешений.

Пятнадцатая глава — хороший рубеж. Вы уже держите массивы, строки, списки, графовые сетки и теперь деревья. Это не случайный прогресс, это системный навык, который заметен интервьюеру сразу.

Полезные ссылки:
- [Invert Binary Tree на LeetCode](https://leetcode.com/problems/invert-binary-tree/)
- [Оглавление книги](./README.md)
