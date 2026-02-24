# 42. Rotting Oranges: поиск в ширину по слоям времени

Эта задача неприятно обманывает в начале: кажется, что нужно «симулировать всё честно», и код сразу становится шумным. На деле здесь одна чистая модель — BFS по минутным слоям.

Суть без лишнего:
- кладём все изначально гнилые апельсины в очередь;
- считаем количество свежих;
- каждый уровень очереди — ровно одна минута;
- заражаем только соседей по четырём направлениям.

Критический момент:
- если свежих не было с самого начала, ответ `0`;
- если после обхода свежие остались, ответ `-1`;
- иначе ответ — число минут, за которые прошли слои.

Сложность:
- время: **O(m × n)**;
- память: **O(m × n)** в худшем случае из-за очереди.

Термины:
- **multi-source BFS** — обход в ширину от множества стартовых точек;
- **time layer** — слой времени;
- **unreachable state** — недостижимое состояние.

Пример на Python:

```python
from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc))
        minutes += 1

    return minutes if fresh == 0 else -1
```

Пример ответа на интервью:

> “I model minutes as BFS layers from all rotten sources at once. Each layer spreads rot to adjacent fresh cells, and leftover fresh cells imply an impossible case.”  
> [«Я моделирую минуты как BFS-слои сразу от всех гнилых источников. Каждый слой заражает соседние свежие клетки, а оставшиеся свежие клетки означают невозможный случай».]

Пара фраз для памяти:
- “One layer, one minute.”  
  [«Один слой — одна минута».]
- “If fresh remains, the model says no.”  
  [«Если свежие остались, модель говорит “нет”».]

Где это в работе: распространение инцидента по сервисной карте, волны обновлений по кластерам, оценка времени охвата при массовых нотификациях.

Вы уже видите важный паттерн: когда система меняется волнами, почти всегда стоит думать слоями, а не отдельными событиями.

Полезные ссылки:
- [Rotting Oranges на LeetCode](https://leetcode.com/problems/rotting-oranges/)
- [Глава про Find Minimum in Rotated Sorted Array](./41_find_minimum_in_rotated_sorted_array_binary_pivot_ru.md)
- [Оглавление книги](./README.md)
