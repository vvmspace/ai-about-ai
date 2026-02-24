# 14. Number of Islands: компоненты связности на сетке

Это графовая задача под маской матрицы. Каждая «островная» область — отдельная компонента связности.

План:
1. идём по всем клеткам;
2. при встрече `'1'` увеличиваем счётчик островов;
3. DFS/BFS помечает всю компоненту как посещённую.

Сложность:
- время: **O(m*n)**;
- память: **O(m*n)** в худшем случае из-за глубины обхода.

Термины: **implicit graph**, **flood fill**, **connected component**.

```go
package main

func numIslands(grid [][]byte) int {
	rows, cols := len(grid), len(grid[0])
	var dfs func(int, int)

	dfs = func(r, c int) {
		if r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != '1' {
			return
		}
		grid[r][c] = '0' // Пометка посещения.
		dfs(r+1, c)
		dfs(r-1, c)
		dfs(r, c+1)
		dfs(r, c-1)
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

> “I model the grid as an implicit graph and count connected components with flood fill.”

- [Number of Islands на LeetCode](https://leetcode.com/problems/number-of-islands/)
- [Оглавление книги](./README.md)
