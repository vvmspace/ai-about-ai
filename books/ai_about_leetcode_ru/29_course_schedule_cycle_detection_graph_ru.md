# 29. Course Schedule: цикл зависимостей и границы выполнимости

Вот где интервью начинает напоминать реальную инженерию. Нужно не «обойти граф», а ответить: можно ли вообще завершить план, если есть зависимости.

Ключевая мысль:
- курсы — вершины;
- prerequisites — направленные рёбра;
- если в графе есть цикл, выполнить всё невозможно.

Практичный метод — топологическая сортировка через indegree (Kahn):
- считаем входящие степени;
- кладём в очередь вершины с indegree = 0;
- снимаем их, уменьшая indegree у соседей;
- если обработали все вершины, ответ `true`, иначе `false`.

Сложность:
- время: **O(V + E)**;
- память: **O(V + E)**.

Термины:
- **DAG** — направленный ациклический граф;
- **in-degree accounting** — учёт числа входящих зависимостей;
- **feasibility check** — проверка выполнимости плана.

Пример на Rust:

```rust
use std::collections::VecDeque;

pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
    let n = num_courses as usize;
    let mut graph = vec![Vec::new(); n];
    let mut indegree = vec![0; n];

    for edge in prerequisites {
        let course = edge[0] as usize;
        let prereq = edge[1] as usize;
        graph[prereq].push(course);
        indegree[course] += 1;
    }

    let mut q = VecDeque::new();
    for i in 0..n {
        if indegree[i] == 0 {
            q.push_back(i);
        }
    }

    let mut taken = 0;
    while let Some(v) = q.pop_front() {
        taken += 1;
        for &next in &graph[v] {
            indegree[next] -= 1;
            if indegree[next] == 0 {
                q.push_back(next);
            }
        }
    }

    taken == n
}
```

Интервью-ответ:

> “I convert prerequisites into a directed graph and run Kahn’s topological process. If I can consume all nodes, the schedule is feasible; if not, a cycle blocks completion.”  
> [«Я преобразую prerequisites в ориентированный граф и запускаю процесс топологической сортировки Кана. Если удаётся обработать все вершины, расписание выполнимо; если нет, завершение блокирует цикл».]

Фразы для фиксации:
- “No zero in-degree, no progress.”  
  [«Нет вершин с нулевой входящей степенью — нет прогресса».]
- “Cycles are promises you cannot keep.”  
  [«Циклы — это обещания, которые невозможно выполнить».]

Где это на практике: пайплайны сборки, зависимости сервисов, порядок миграций баз данных.

И вот приятный результат: теперь графы перестали быть абстракцией из учебника. Вы видите в них контракт выполнимости системы — и это очень сильный сигнал на интервью.

Полезные ссылки:
- [Course Schedule на LeetCode](https://leetcode.com/problems/course-schedule/)
- [Глава про Meeting Rooms II](./28_meeting_rooms_ii_min_heap_timeline_ru.md)
- [Оглавление книги](./README.md)
