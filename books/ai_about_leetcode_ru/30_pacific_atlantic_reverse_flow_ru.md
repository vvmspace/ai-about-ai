# 30. Pacific Atlantic Water Flow: думать от границ, а не от каждой клетки

Обычно кандидат начинает с каждой точки и тонет в повторах. Здесь выигрыш приходит, когда вы переворачиваете направление мысли: вода «течёт вниз», но обход мы делаем «вверх» от океанов.

Суть:
- запускаем обход от границ Тихого океана;
- отдельно запускаем обход от границ Атлантики;
- в обходе идём только в соседей с высотой **не ниже** текущей;
- пересечение двух множеств достижимости и есть ответ.

Сложность:
- время: **O(m × n)**;
- память: **O(m × n)** на visited-массивы.

Термины:
- **reverse reachability** — достижимость в обратном направлении потока;
- **boundary-seeded traversal** — запуск обхода от границ;
- **set intersection** — пересечение достижимых клеток.

Пример на Python:

```python
from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])
    pac = [[False] * cols for _ in range(rows)]
    atl = [[False] * cols for _ in range(rows)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r: int, c: int, seen: List[List[bool]]) -> None:
        seen[r][c] = True
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            if seen[nr][nc] or heights[nr][nc] < heights[r][c]:
                continue
            dfs(nr, nc, seen)

    for r in range(rows):
        dfs(r, 0, pac)
        dfs(r, cols - 1, atl)
    for c in range(cols):
        dfs(0, c, pac)
        dfs(rows - 1, c, atl)

    ans = []
    for r in range(rows):
        for c in range(cols):
            if pac[r][c] and atl[r][c]:
                ans.append([r, c])
    return ans
```

Интервью-ответ:

> “I solve it as two reverse graph traversals from ocean borders. Cells reachable from both traversals are exactly the cells that can flow to both oceans.”  
> [«Я решаю задачу как два обратных обхода графа от границ океанов. Клетки, достижимые в обоих обходах, — это ровно клетки, из которых вода может попасть в оба океана».]

Фразы для запоминания:
- “Start from constraints, not from brute force.”  
  [«Стартуй от ограничений, а не от brute force».]
- “Reverse the flow, simplify the proof.”  
  [«Переверни поток — упрости доказательство».]

Где это в работе: анализ достижимости в сетях, распространение прав доступа по графу зависимостей, оценка зон влияния в карте сервисов.

Вы только что сделали сильный инженерный шаг: не «быстрее перебираю», а «иначе моделирую». Это именно тот уровень, который резко поднимает вашу ценность на интервью.

Полезные ссылки:
- [Pacific Atlantic Water Flow на LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- [Глава про Course Schedule](./29_course_schedule_cycle_detection_graph_ru.md)
- [Оглавление книги](./README.md)
