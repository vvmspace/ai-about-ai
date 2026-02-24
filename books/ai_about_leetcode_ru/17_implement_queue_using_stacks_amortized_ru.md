# 17. Implement Queue using Stacks: симуляция структуры

Здесь проверяют, понимаете ли вы амортизированную сложность, а не просто API. Очередь собирается из двух стеков: `in` и `out`.

Идея:
- `push` кладёт элементы в `in`;
- `pop/peek` читают из `out`;
- если `out` пуст, переливаем в него всё из `in`.

Сложность:
- `push`: **O(1)**;
- `pop/peek`: **амортизированно O(1)**.

Термины: **amortized analysis**, **lazy transfer**, **FIFO emulation**.

```javascript
class MyQueue {
  constructor() {
    this.in = [];
    this.out = [];
  }

  push(x) {
    this.in.push(x); // Новые элементы идут во входной стек.
  }

  shiftIfNeeded() {
    if (this.out.length === 0) {
      while (this.in.length) {
        this.out.push(this.in.pop()); // Перенос меняет порядок на FIFO.
      }
    }
  }

  pop() {
    this.shiftIfNeeded();
    return this.out.pop();
  }

  peek() {
    this.shiftIfNeeded();
    return this.out[this.out.length - 1];
  }

  empty() {
    return this.in.length === 0 && this.out.length === 0;
  }
}
```

> “I implement FIFO semantics with two LIFO structures and a lazy transfer, which yields amortized constant-time operations.”

- [Implement Queue using Stacks на LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)
- [Оглавление книги](./README.md)
