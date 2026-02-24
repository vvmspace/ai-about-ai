# 14. Number of Islands: DFS/BFS в сетке без хаоса

На собеседовании эта задача часто ломает не алгоритм, а мышление. Люди видят «матрицу» и начинают импровизировать без модели.

Строго говоря, это граф:
- каждая клетка `1` — вершина;
- соседство по четырём направлениям — рёбра;
- каждый новый не посещённый кусок суши — новая компонента связности, то есть остров.

Дальше всё дисциплинированно: идём по матрице, запускаем DFS или BFS из каждой новой суши и помечаем весь остров посещённым.

Сложность:
- время: **O(m * n)**;
- память: **O(m * n)** в худшем случае для стека/очереди.

Неочевидные термины:
- **connected component** — максимальная связная группа вершин;
- **flood fill** — заливка области обходом соседей;
- **visited marking strategy** — способ пометки посещённых узлов, отдельной матрицей или in-place.

Пример на Go (BFS):

```go
package main

func numIslands(grid [][]byte) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}

	rows, cols := len(grid), len(grid[0])
	count := 0
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] != '1' {
				continue
			}

			count++
			queue := [][2]int{{r, c}}
			grid[r][c] = '0'

			for len(queue) > 0 {
				cell := queue[0]
				queue = queue[1:]

				for _, d := range dirs {
					nr, nc := cell[0]+d[0], cell[1]+d[1]
					if nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1' {
						grid[nr][nc] = '0'
						queue = append(queue, [2]int{nr, nc})
					}
				}
			}
		}
	}

	return count
}
```

Интервью-ответ:

> “I model the grid as an implicit graph and count connected components. Every time I see an unvisited land cell, I run BFS/DFS to consume that whole island. The scan is linear in the number of cells.”  
> [«Я моделирую сетку как неявный граф и считаю компоненты связности. Каждый раз, когда вижу непосещённую сушу, запускаю BFS/DFS и поглощаю весь остров. Скан остаётся линейным по числу клеток».]

Пара фраз:
- “The grid is just a graph with polite disguise.”  
  [«Сетка — это просто граф в вежливой маскировке».]
- “Mark once, never revisit.”  
  [«Пометь один раз и не возвращайся».]

Где это в работе: сегментация областей на картах, кластеризация инцидентов по сетевым зонам, анализ связных регионов в изображениях.

Полезные ссылки:
- [Number of Islands на LeetCode](https://leetcode.com/problems/number-of-islands/)
- [Оглавление книги](./README.md)
