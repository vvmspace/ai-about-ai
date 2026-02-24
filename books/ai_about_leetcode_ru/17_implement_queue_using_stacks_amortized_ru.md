# 17. Implement Queue using Stacks: симуляция структуры

Очередь можно собрать из двух стеков: `in` для новых элементов и `out` для выдачи. Когда `out` пуст, переливаем из `in` в `out`.

Сложность:
- `push`: **O(1)**;
- `pop/peek`: **амортизированно O(1)**.

Термины: **amortized analysis**, **lazy transfer**, **interface emulation**.

```javascript
class MyQueue {
  constructor() {
    this.in = [];
    this.out = [];
  }

  push(x) {
    this.in.push(x);
  }

  shiftIfNeeded() {
    if (this.out.length === 0) {
      while (this.in.length) {
        this.out.push(this.in.pop());
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

> “I use two stacks with lazy transfer, which preserves FIFO behaviour and yields amortized constant-time operations.”

- [Implement Queue using Stacks на LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)
- [Оглавление книги](./README.md)
