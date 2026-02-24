# 49. Alien Dictionary: топологическая сортировка порядка символов

Это уже задача на зрелость: нужно восстановить порядок алфавита из отсортированного словаря. Ошибка в одном краевом случае уничтожает корректность.

Шаги:
- строим граф зависимостей между символами по первой различающейся букве соседних слов;
- считаем входящие степени;
- запускаем topological sort (обычно Kahn BFS).

Обязательная проверка:
- если длинное слово идёт раньше своего префикса (`"abc"` перед `"ab"`), вход некорректен, ответ пустой.

Сложность:
- время: **O(C + E)**, где `C` — число уникальных символов;
- память: **O(C + E)**.

Термины:
- **precedence edge** — ребро приоритета;
- **in-degree** — входящая степень;
- **cycle detection by output length** — обнаружение цикла по длине результата.

Пример на Go:

```go
package main

func alienOrder(words []string) string {
    graph := map[byte]map[byte]bool{}
    indeg := map[byte]int{}

    for _, w := range words {
        for i := 0; i < len(w); i++ {
            if _, ok := graph[w[i]]; !ok {
                graph[w[i]] = map[byte]bool{}
            }
            if _, ok := indeg[w[i]]; !ok {
                indeg[w[i]] = 0
            }
        }
    }

    for i := 0; i+1 < len(words); i++ {
        a, b := words[i], words[i+1]
        if len(a) > len(b) && a[:len(b)] == b {
            return ""
        }
        for j := 0; j < len(a) && j < len(b); j++ {
            if a[j] != b[j] {
                if !graph[a[j]][b[j]] {
                    graph[a[j]][b[j]] = true
                    indeg[b[j]]++
                }
                break
            }
        }
    }

    q := make([]byte, 0)
    for ch, d := range indeg {
        if d == 0 {
            q = append(q, ch)
        }
    }

    out := make([]byte, 0, len(indeg))
    for len(q) > 0 {
        ch := q[0]
        q = q[1:]
        out = append(out, ch)
        for nxt := range graph[ch] {
            indeg[nxt]--
            if indeg[nxt] == 0 {
                q = append(q, nxt)
            }
        }
    }

    if len(out) != len(indeg) {
        return ""
    }
    return string(out)
}
```

Пример ответа на интервью:

> “I derive ordering constraints from first mismatches between adjacent words and then run topological sort. Invalid prefix order and cycles both produce empty output.”  
> [«Я извлекаю ограничения порядка по первой несовпадающей паре символов у соседних слов и затем запускаю топологическую сортировку. Неверный префиксный порядок и циклы оба дают пустой результат».]

Пара фраз для памяти:
- “Constraints first, alphabet second.”  
  [«Сначала ограничения, потом алфавит».]
- “No acyclic order, no answer.”  
  [«Нет ацикличного порядка — нет ответа».]

Где это в работе: вычисление порядка миграций, зависимостей сборки, этапов пайплайна по частичным правилам.

Полезные ссылки:
- [Alien Dictionary на LeetCode](https://leetcode.com/problems/alien-dictionary/)
- [Глава про Word Ladder](./48_word_ladder_bfs_pattern_index_ru.md)
- [Оглавление книги](./README.md)
