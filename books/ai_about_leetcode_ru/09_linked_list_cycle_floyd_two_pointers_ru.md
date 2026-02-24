# 09. Linked List Cycle: медленный и быстрый указатели

У задачи про цикл в списке красивый эффект: решение выглядит как фокус, но основано на строгой математике движения.

Идея Floyd (tortoise and hare):
- `slow` двигается на 1 шаг;
- `fast` двигается на 2 шага;
- если цикл есть, они неизбежно встретятся;
- если `fast` дошёл до `null`, цикла нет.

Сложность:
- время: **O(n)**;
- память: **O(1)**.

Неочевидные термины:
- **phase offset** — сдвиг фаз между указателями;
- **modular distance** — расстояние по модулю длины цикла;
- **pointer chasing** — последовательный переход по ссылкам без случайного доступа.

Пример на Python:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # +1 шаг
        fast = fast.next.next     # +2 шага

        if slow is fast:
            return True           # Встреча возможна только при наличии цикла.

    return False                  # Быстрый указатель упёрся в конец.
```

Интервью-ответ:

> “I use Floyd’s two-pointer technique: if a cycle exists, relative speed guarantees intersection; if not, the fast pointer reaches null. This gives linear time and constant memory without hash storage.”  
> [«Я использую технику Флойда с двумя указателями: если цикл существует, относительная скорость гарантирует встречу; если нет, быстрый указатель дойдёт до null. Это даёт линейное время и константную память без хеш-хранилища».]

Пара фраз:
- “Relative speed proves convergence.”  
  [«Относительная скорость доказывает сходимость».]
- “No extra memory, no compromise.”  
  [«Без дополнительной памяти, без компромисса».]

Где это в работе: обнаружение циклических ссылок в графах зависимостей, защита от бесконечных цепочек редиректов, анализ цепочек ретраев в очередях.

Полезные ссылки:
- [Linked List Cycle на LeetCode](https://leetcode.com/problems/linked-list-cycle/)
- [Оглавление книги](./README.md)
