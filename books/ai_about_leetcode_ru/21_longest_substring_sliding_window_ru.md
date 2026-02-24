# 21. Longest Substring Without Repeating Characters: скользящее окно под контролем

Если хотите быстро понять уровень кандидата по строкам, дайте ему эту задачу. Почти все знают идею окна, но не все держат инвариант.

Инвариант окна: в текущем диапазоне нет повторяющихся символов.
Когда новый символ уже встречался внутри окна, двигаем левую границу вправо до восстановления условия.

Сложность:
- время: **O(n)**;
- память: **O(min(n, k))**, где `k` — размер алфавита.

Неочевидные термины:
- **sliding window invariant** — условие, которое обязано быть истинным в каждом шаге;
- **last seen index** — последняя позиция символа для прыжка левой границы;
- **window length maximization** — поддержка максимальной длины валидного окна.

Пример на Rust:

```rust
use std::collections::HashMap;

pub fn length_of_longest_substring(s: String) -> i32 {
    let mut last = HashMap::<char, usize>::new();
    let mut left = 0usize;
    let mut best = 0usize;

    for (right, ch) in s.chars().enumerate() {
        if let Some(&idx) = last.get(&ch) {
            if idx >= left {
                left = idx + 1;
            }
        }

        last.insert(ch, right);
        best = best.max(right - left + 1);
    }

    best as i32
}
```

Интервью-ответ:

> “I maintain a valid sliding window with no duplicates and update the left boundary using the last seen index map. Each index moves forward at most once, so total complexity is linear.”  
> [«Я поддерживаю валидное скользящее окно без повторов и обновляю левую границу через карту последних вхождений. Каждый индекс двигается вперёд не более одного раза, поэтому итоговая сложность линейная».]

Пара фраз:
- “Window validity comes first.”  
  [«Сначала валидность окна».]
- “Move boundaries, not emotions.”  
  [«Двигай границы, а не эмоции».]

Где это в работе: поиск самого длинного уникального токена в потоке, анализ сессий без повторов событий, контроль повторяемости в пользовательских цепочках.

Полезные ссылки:
- [Longest Substring Without Repeating Characters на LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [Глава про Binary Search](./08_binary_search_boundary_discipline_ru.md)
- [Оглавление книги](./README.md)
