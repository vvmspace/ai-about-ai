# 08. Binary Search: дисциплина границ

Бинарный поиск знают все. Ломают его тоже почти все. Ошибка обычно не в идее, а в границах: `left`, `right`, условие цикла, выбор полуинтервала.

Рабочая модель: используем полуинтервал `[left, right)`.
- `left` включён;
- `right` исключён;
- цикл идёт пока `left < right`.

Это снимает половину off-by-one ошибок.

Сложность:
- время: **O(log n)**;
- память: **O(1)**.

Неочевидные термины:
- **search invariant** — утверждение, которое сохраняется после каждого шага;
- **monotonic predicate** — монотонное условие, по которому можно делить пространство пополам;
- **lower bound** — первая позиция, где условие становится истинным.

Пример на Rust:

```rust
pub fn binary_search(nums: &[i32], target: i32) -> i32 {
    let mut left = 0usize;
    let mut right = nums.len(); // Полуинтервал [left, right)

    while left < right {
        let mid = left + (right - left) / 2; // Избегаем переполнения формулы.

        if nums[mid] < target {
            left = mid + 1; // Цель правее.
        } else if nums[mid] > target {
            right = mid; // Цель левее, mid исключаем.
        } else {
            return mid as i32; // Найдено.
        }
    }

    -1
}
```

Интервью-ответ:

> “I keep a half-open interval and maintain an explicit search invariant. Each comparison removes half of the remaining candidates, so we get logarithmic time with constant space.”  
> [«Я держу полуоткрытый интервал и явно поддерживаю инвариант поиска. Каждое сравнение отбрасывает половину оставшихся кандидатов, поэтому получаем логарифмическое время и константную память».]

Пара фраз:
- “Boundaries are the algorithm.”  
  [«Границы — это и есть алгоритм».]
- “Half-open intervals reduce ambiguity.”  
  [«Полуоткрытые интервалы уменьшают неоднозначность».]

Где это в работе: поиск порога в SLA-метриках, бинарный подбор параметров, нахождение первой «ломающейся» версии в CI.

Полезные ссылки:
- [Binary Search на LeetCode](https://leetcode.com/problems/binary-search/)
- [Оглавление книги](./README.md)
