# 14. Number of Islands: DFS/BFS на сетке

Сетка — это неявный граф. Каждый кусок суши — компонент связности. Значит, задача сводится к подсчёту компонент.

Сложность:
- время: **O(m*n)**;
- память: **O(m*n)** в худшем случае на стек/очередь обхода.

Термины: **connected components**, **flood fill**, **4-neighborhood**.

```go
package main

func numIslands(grid [][]byte) int {
	rows, cols := len(grid), len(grid[0])
	var dfs func(int, int)
	dfs = func(r, c int) {
		if r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != '1' {
			return
		}
		grid[r][c] = '0' // Помечаем посещённой.
		dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
	}
	count := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] == '1' {
				count++
				dfs(r, c)
			}
		}
	}
	return count
}
```

> “I treat the grid as an implicit graph and count connected components via flood fill.”

- [Number of Islands на LeetCode](https://leetcode.com/problems/number-of-islands/)
- [Оглавление книги](./README.md)
