# 12. Reverse Linked List: разворот структуры под контролем инварианта

Развернуть связный список — не про «поменять стрелочки». Это тест на то, как вы держите инвариант при мутации указателей.

Рабочая рамка:
- `prev` хранит уже перевёрнутую часть;
- `curr` указывает на текущий узел;
- `next_node` временно спасает хвост, чтобы не потерять список.

На каждом шаге меняем одно ребро и сдвигаем три указателя.

Сложность:
- время: **O(n)**;
- память: **O(1)**.

Неочевидные термины:
- **in-place mutation** — изменение структуры без дополнительного контейнера;
- **pointer safety window** — короткий участок кода, где важно не потерять доступ к данным;
- **loop invariant** — условие, которое истинно до и после каждой итерации.

Пример на Python:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev
```

Интервью-ответ:

> “I reverse the list iteratively with three pointers and a strict invariant: `prev` is always the reversed prefix, `curr` is the node being processed. That guarantees linear time and constant space.”  
> [«Я разворачиваю список итеративно тремя указателями и строгим инвариантом: `prev` всегда является уже развёрнутым префиксом, `curr` — обрабатываемым узлом. Это гарантирует линейное время и константную память».]

Пара фраз:
- “Protect the tail before rewiring.”  
  [«Сначала защити хвост, потом перенастраивай связи».]
- “Invariants prevent pointer panic.”  
  [«Инварианты предотвращают панику указателей».]

Где это в работе: разворот цепочек событий, нормализация порядка операций в ETL, обработка пользовательской истории в обратной хронологии.

Полезные ссылки:
- [Reverse Linked List на LeetCode](https://leetcode.com/problems/reverse-linked-list/)
- [Глава про Linked List Cycle](./09_linked_list_cycle_floyd_two_pointers_ru.md)
- [Оглавление книги](./README.md)
