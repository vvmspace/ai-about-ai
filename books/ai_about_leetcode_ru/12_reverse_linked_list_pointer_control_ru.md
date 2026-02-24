# 12. Reverse Linked List: контроль указателей под давлением

На собеседовании эту задачу дают, чтобы проверить холодную технику работы со ссылками. Одна ошибка — и список потерян.

Инвариант: `prev` — уже развёрнутый префикс, `cur` — ещё не обработанная часть.

Сложность:
- время: **O(n)**;
- память: **O(1)**.

Термины: **pointer rewiring**, **loop invariant**, **in-place update**.

```javascript
function reverseList(head) {
  let prev = null;
  let cur = head;

  while (cur) {
    const next = cur.next; // Сохраняем оставшийся хвост.
    cur.next = prev;       // Переворачиваем ребро.
    prev = cur;            // Сдвигаем границу обработанного участка.
    cur = next;
  }

  return prev;
}
```

> “I rewire pointers in-place while preserving a strict processed/unprocessed invariant.”

- [Reverse Linked List на LeetCode](https://leetcode.com/problems/reverse-linked-list/)
- [Оглавление книги](./README.md)
