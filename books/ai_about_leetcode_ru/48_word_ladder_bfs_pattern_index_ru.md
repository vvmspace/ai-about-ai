# 48. Word Ladder: кратчайший путь в словарном графе

На поверхности это «игра со словами». Внутри — чистый shortest path в неявном графе, где узлы это слова, а рёбра — односимвольные замены.

Эффективная модель:
- строим индекс шаблонов: `h*t -> [hot, hit, ...]`;
- запускаем BFS от `beginWord`;
- первый раз, когда дошли до `endWord`, даёт минимальное число шагов.

Почему индекс обязателен:
- наивная генерация соседей через сравнение со всеми словами слишком медленная;
- шаблонный индекс превращает поиск соседей в быстрые выборки.

Сложность:
- время: примерно **O(N × L²)** с учётом построения и обхода;
- память: **O(N × L)**.

Термины:
- **implicit graph** — неявный граф;
- **pattern bucket** — корзина по шаблону;
- **shortest transformation** — кратчайшая трансформация.

Пример на Python:

```python
from collections import defaultdict, deque
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    L = len(beginWord)
    buckets = defaultdict(list)
    for w in wordList:
        for i in range(L):
            buckets[w[:i] + '*' + w[i+1:]].append(w)

    q = deque([(beginWord, 1)])
    seen = {beginWord}

    while q:
        word, dist = q.popleft()
        if word == endWord:
            return dist

        for i in range(L):
            key = word[:i] + '*' + word[i+1:]
            for nxt in buckets[key]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, dist + 1))
            buckets[key] = []

    return 0
```

Пример ответа на интервью:

> “I model words as nodes in an implicit graph and run BFS for shortest path. Pattern buckets let me find neighbours efficiently instead of scanning the whole dictionary.”  
> [«Я моделирую слова как узлы неявного графа и запускаю BFS для кратчайшего пути. Корзины шаблонов позволяют находить соседей эффективно, а не сканировать весь словарь».]

Пара фраз для памяти:
- “BFS gives shortest by construction.”  
  [«BFS даёт кратчайший путь по построению».]
- “Index neighbours or pay the cost.”  
  [«Либо индексируй соседей, либо плати ценой времени».]

Где это в работе: трансформация конфигураций по шагам, поиск кратчайших маршрутов миграции данных, планирование цепочек исправлений.

Полезные ссылки:
- [Word Ladder на LeetCode](https://leetcode.com/problems/word-ladder/)
- [Глава про Regular Expression Matching](./47_regular_expression_matching_dynamic_programming_grid_ru.md)
- [Оглавление книги](./README.md)
