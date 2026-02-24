# 13. Top K Frequent Elements: куча против bucket-подхода

Вопрос звучит просто: «дай top-k по частоте». Ловушка в том, что интервьюер проверяет не код, а зрелость выбора между двумя корректными стратегиями.

Шаг 1 всегда одинаковый: считаем частоты через hash map.
Шаг 2 уже про trade-off:
- min-heap размера `k` — универсально и предсказуемо;
- bucket sort по частотам — линейно, если частоты ограничены `n`.

Сложность heap-подхода:
- время: **O(n log k)**;
- память: **O(n)**.

Сложность bucket-подхода:
- время: **O(n)**;
- память: **O(n)**.

Неочевидные термины:
- **selection algorithm** — алгоритм выбора части элементов без полной сортировки;
- **frequency bucket** — корзина элементов с одинаковой частотой;
- **asymptotic trade-off** — обмен между асимптотикой и практическими константами.

Пример на Rust (heap):

```rust
use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};

pub fn top_k_frequent(nums: Vec<i32>, k: usize) -> Vec<i32> {
    let mut freq = HashMap::new();
    for n in nums {
        *freq.entry(n).or_insert(0) += 1;
    }

    let mut heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();

    for (num, count) in freq {
        heap.push(Reverse((count, num)));
        if heap.len() > k {
            heap.pop();
        }
    }

    heap.into_iter().map(|Reverse((_, num))| num).collect()
}
```

Интервью-ответ:

> “I split the problem into counting and selection. Counting is a hash map. Selection is either a size-k min-heap for robust performance, or bucket traversal when I want linear time under standard constraints.”  
> [«Я делю задачу на подсчёт и выбор. Подсчёт делается через hash map. Выбор — либо min-heap размера k для устойчивой производительности, либо обход bucket-структуры, когда нужна линейная асимптотика при стандартных ограничениях».]

Пара фраз:
- “Count first. Optimise selection second.”  
  [«Сначала считай. Потом оптимизируй выбор».]
- “Top-k is about discipline, not decoration.”  
  [«Top-k — это про дисциплину, а не украшения».]

Где это в работе: топ поисковых запросов за период, самые частые типы ошибок в логах, горячие категории в рекомендательных системах.

Вы уже на тринадцатой главе, и это отличный знак: базовые структуры данных больше не выглядят случайным набором тем. Они начинают складываться в систему, которая даёт вам спокойствие на собеседовании.

Полезные ссылки:
- [Top K Frequent Elements на LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)
- [Глава про Contains Duplicate](./04_contains_duplicate_hashset_signal_ru.md)
- [Оглавление книги](./README.md)
