# 25. Merge Intervals: сортировка интервалов как рабочий рефлекс backend

Интервью-вопрос простой: «слить пересекающиеся интервалы». Реальный вопрос глубже: умеете ли вы сначала нормализовать данные, а потом делать sweep без суеты.

Алгоритм:
- сортируем интервалы по старту;
- держим текущий интервал в результате;
- если новый пересекается — расширяем конец;
- если нет — начинаем новый интервал.

Сложность:
- время: **O(n log n)** из-за сортировки;
- память: **O(n)** на результат.

Неочевидные термины:
- **interval normalization** — приведение входа к упорядоченной форме;
- **sweep line mindset** — последовательный проход с поддержкой активного состояния;
- **overlap coalescing** — объединение пересекающихся диапазонов в один.

Пример на Rust:

```rust
pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    if intervals.is_empty() {
        return vec![];
    }

    intervals.sort_by_key(|v| v[0]);
    let mut merged: Vec<Vec<i32>> = vec![intervals[0].clone()];

    for interval in intervals.into_iter().skip(1) {
        let last = merged.last_mut().unwrap();

        if interval[0] <= last[1] {
            last[1] = last[1].max(interval[1]);
        } else {
            merged.push(interval);
        }
    }

    merged
}
```

Интервью-ответ:

> “I sort intervals by start and perform a linear sweep with one active interval. Overlaps extend the active range; disjoint intervals are flushed to output. This yields predictable correctness and complexity.”  
> [«Я сортирую интервалы по началу и выполняю линейный sweep с одним активным интервалом. Пересечения расширяют активный диапазон, непересекающиеся интервалы сбрасываются в результат. Это даёт предсказуемую корректность и сложность».]

Пара фраз:
- “Sort first, merge calmly.”  
  [«Сначала сортируй, потом спокойно сливай».]
- “One active interval, full control.”  
  [«Один активный интервал — полный контроль».]

Где это в работе: объединение слотов бронирования, консолидация биллинговых периодов, свёртка окон инцидентов.

25-я глава — приятная точка ускорения: вы уже уверенно проходите задачи, где важны не трюки, а структурное мышление. Это как раз тот уровень, который отличает «знаю решения» от «умею проектировать ответ».

Полезные ссылки:
- [Merge Intervals на LeetCode](https://leetcode.com/problems/merge-intervals/)
- [Глава про Search in Rotated Sorted Array](./23_search_rotated_sorted_array_binary_logic_ru.md)
- [Оглавление книги](./README.md)
