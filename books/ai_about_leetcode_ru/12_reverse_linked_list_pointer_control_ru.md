# 12. Reverse Linked List: разворот под контролем инварианта

Разворот списка — упражнение на pointer hygiene. Инвариант: `prev` хранит уже развёрнутую часть, `cur` — необработанный хвост.

Сложность:
- время: **O(n)**;
- память: **O(1)**.

Термины: **pointer rewiring**, **loop invariant**, **in-place mutation**.

```javascript
function reverseList(head) {
  let prev = null;
  let cur = head;

  while (cur) {
    const next = cur.next; // Сохраняем хвост.
    cur.next = prev;       // Переворачиваем ссылку.
    prev = cur;            // Сдвигаем prev.
    cur = next;            // Сдвигаем cur.
  }

  return prev;
}
```

> “I rewire pointers in-place while preserving a strict invariant between processed and unprocessed segments.”

- [Reverse Linked List на LeetCode](https://leetcode.com/problems/reverse-linked-list/)
- [Оглавление книги](./README.md)
