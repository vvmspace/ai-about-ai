# 26. Insert Interval: аккуратная вставка без повторного хаоса

С виду это «ещё один merge intervals». На практике это проверка, держите ли вы голову холодной, когда к отсортированному потоку добавляют один новый диапазон.

Идея простая:
- сначала добавляем все интервалы, которые точно заканчиваются до нового;
- затем сливаем всё, что пересекается с новым;
- потом дописываем хвост без изменений.

Сложность:
- время: **O(n)**, потому что проходим список один раз;
- память: **O(n)** на результирующий список.

Термины, которые полезно знать:
- **merge window** — текущий диапазон, который расширяется при пересечениях;
- **disjoint prefix/suffix** — гарантированно непересекающиеся части до и после окна;
- **single-pass merge** — слияние за один линейный проход.

Пример на Python:

```python
from typing import List

def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    res = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1

    start, end = new_interval
    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    res.append([start, end])

    while i < n:
        res.append(intervals[i])
        i += 1

    return res
```

Интервью-ответ:

> “I keep the original order and merge only where overlap is possible. Everything before and after that window stays untouched, which gives a linear and auditable solution.”  
> [«Я сохраняю исходный порядок и сливаю только там, где возможно пересечение. Всё до и после этого окна остаётся неизменным, поэтому решение линейное и проверяемое».]

Две фразы для памяти:
- “Merge the middle, trust the edges.”  
  [«Сливай середину, доверяй краям».]
- “One pass. No drama.”  
  [«Один проход. Без драмы».]

Где это встречается в работе: обновление календарных окон, корректировка SLA-периодов, вставка нового промо-слота в уже рассчитанный таймлайн.

Вы уже чувствуете эффект: ещё недавно такие задачи казались «про аккуратность в коде», а теперь это просто контроль состояния на каждом шаге. Именно так и растёт интервью-уверенность.

Полезные ссылки:
- [Insert Interval на LeetCode](https://leetcode.com/problems/insert-interval/)
- [Глава про Merge Intervals](./25_merge_intervals_sort_and_sweep_ru.md)
- [Оглавление книги](./README.md)
