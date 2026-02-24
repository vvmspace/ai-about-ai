# 18. Kth Smallest Element in a BST: inorder как отсортированный поток

Эта задача выглядит как «найди k-й элемент». На деле это вопрос: понимаете ли вы, что BST уже хранит порядок в своей структуре.

Ключевая мысль: inorder-обход BST даёт значения по возрастанию.
Значит, мы идём inorder и останавливаемся, когда счётчик доходит до `k`.

Сложность:
- время: **O(h + k)** в среднем, если останавливаемся рано;
- память: **O(h)** на стек рекурсии/итерации.

Неочевидные термины:
- **inorder stream** — последовательность значений, получаемая inorder-обходом;
- **early termination** — ранняя остановка, когда ответ найден до полного обхода;
- **order statistic** — элемент с заданным рангом в отсортированном наборе.

Пример на Python (итеративно):

```python
def kth_smallest(root, k):
    stack = []
    node = root

    while True:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val

        node = node.right
```

Интервью-ответ:

> “In a BST, inorder traversal is naturally sorted. I perform iterative inorder and stop exactly at the k-th visit, which avoids scanning irrelevant nodes.”  
> [«В BST inorder-обход естественно отсортирован. Я делаю итеративный inorder и останавливаюсь ровно на k-м посещении, не сканируя лишние узлы».]

Пара фраз:
- “Order is already in the tree.”  
  [«Порядок уже встроен в дерево».]
- “Traverse only as far as needed.”  
  [«Обходи ровно столько, сколько нужно».]

Где это в работе: выбор top-N по рейтингу, выбор медианного приоритета в дереве задач, ранжирование конфигураций по весу.

Полезные ссылки:
- [Kth Smallest Element in a BST на LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [Глава про LCA в BST](./16_lca_bst_order_property_ru.md)
- [Оглавление книги](./README.md)
