# 17. Implement Queue using Stacks: амортизированная стоимость без самообмана

Интервьюер даёт две структуры и просит симулировать третью. Это не трюк, это проверка инженерного контроля над абстракциями.

Идея:
- `inStack` хранит новые элементы;
- `outStack` отдаёт элементы на `pop/peek`;
- когда `outStack` пуст, переливаем в него всё из `inStack`.

Каждый элемент переносится максимум один раз туда и один раз обратно по операциям жизненного цикла. Поэтому амортизированно всё получается O(1).

Сложность:
- `push`: **O(1)**;
- `pop/peek`: амортизированно **O(1)**;
- память: **O(n)**.

Неочевидные термины:
- **amortized analysis** — оценка средней стоимости по длинной серии операций;
- **lazy transfer** — перенос данных только когда это действительно нужно;
- **operational burst** — редкая дорогая операция, окупаемая множеством дешёвых.

Пример на Rust:

```rust
#[derive(Default)]
pub struct MyQueue {
    in_stack: Vec<i32>,
    out_stack: Vec<i32>,
}

impl MyQueue {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn push(&mut self, x: i32) {
        self.in_stack.push(x);
    }

    fn shift_if_needed(&mut self) {
        if self.out_stack.is_empty() {
            while let Some(v) = self.in_stack.pop() {
                self.out_stack.push(v);
            }
        }
    }

    pub fn pop(&mut self) -> i32 {
        self.shift_if_needed();
        self.out_stack.pop().unwrap()
    }

    pub fn peek(&mut self) -> i32 {
        self.shift_if_needed();
        *self.out_stack.last().unwrap()
    }

    pub fn empty(&self) -> bool {
        self.in_stack.is_empty() && self.out_stack.is_empty()
    }
}
```

Интервью-ответ:

> “I use two stacks and defer transfer until output is required. This lazy strategy gives O(1) amortized queue operations because each element is moved a constant number of times across the full sequence.”  
> [«Я использую два стека и откладываю перенос, пока действительно не понадобится выдача. Эта lazy-стратегия даёт O(1) амортизированно, потому что каждый элемент перемещается константное число раз на всей последовательности операций».]

Пара фраз:
- “Amortized is honest over time.”  
  [«Амортизированная оценка честна на длинной дистанции».]
- “Transfer late, pay less often.”  
  [«Переноси поздно, плати реже».]

Где это в работе: буферизация очередей сообщений, батчинг событий перед отправкой, прокси-слой между входным и выходным транспортом.

Полезные ссылки:
- [Implement Queue using Stacks на LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)
- [Оглавление книги](./README.md)
