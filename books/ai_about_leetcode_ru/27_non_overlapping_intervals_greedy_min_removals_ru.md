# 27. Non-overlapping Intervals: жадность, которая действительно доказуема

Вопрос звучит невинно: сколько интервалов удалить, чтобы остальные не пересекались. Под капотом — зрелость в **greedy reasoning**: нужно выбирать не «красивый» интервал, а тот, что оставляет максимум свободы дальше.

Ключ:
- сортируем интервалы по правой границе;
- берём первый как активный;
- если следующий не пересекается — принимаем его;
- если пересекается — увеличиваем счётчик удалений.

Сложность:
- время: **O(n log n)** из-за сортировки;
- память: **O(1)** без учёта входа.

Полезные термины:
- **earliest finish time** — выбор интервала с минимальным концом;
- **feasible set** — множество интервалов без пересечений;
- **removal minimization** — минимизация удалений через максимизацию сохранённых.

Пример на Go:

```go
package main

import "sort"

func eraseOverlapIntervals(intervals [][]int) int {
    if len(intervals) == 0 {
        return 0
    }

    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][1] < intervals[j][1]
    })

    removed := 0
    prevEnd := intervals[0][1]

    for i := 1; i < len(intervals); i++ {
        if intervals[i][0] < prevEnd {
            removed++
        } else {
            prevEnd = intervals[i][1]
        }
    }

    return removed
}
```

Интервью-ответ:

> “I sort by end time and greedily keep intervals that finish earliest. That maximizes room for the remaining choices and directly minimizes removals.”  
> [«Я сортирую по времени окончания и жадно оставляю интервалы, которые заканчиваются раньше. Это максимизирует пространство для следующих выборов и напрямую минимизирует удаления».]

Фразы, которые удобно держать под рукой:
- “Finish earlier, regret less.”  
  [«Заканчивай раньше — меньше сожалений».]
- “Greedy works when options shrink.”  
  [«Жадность работает, когда пространство выбора сужается».]

Рабочий контекст: планирование задач на ограниченных ресурсах, выбор рекламных окон без конфликтов, приоритизация джобов в пакетной обработке.

Вы дошли до момента, где можно не просто написать ответ, а спокойно защитить его доказательство. Это и есть уровень, который интервьюеры запоминают.

Полезные ссылки:
- [Non-overlapping Intervals на LeetCode](https://leetcode.com/problems/non-overlapping-intervals/)
- [Глава про Insert Interval](./26_insert_interval_merge_window_ru.md)
- [Оглавление книги](./README.md)
