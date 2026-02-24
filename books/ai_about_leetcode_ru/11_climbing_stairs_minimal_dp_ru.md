# 11. Climbing Stairs: минимальная динамика без шума

Задача выглядит как школьная комбинаторика, но это идеальная проверка DP-мышления: вы понимаете переход состояния или просто помните формулу.

Переход простой:
`dp[i] = dp[i-1] + dp[i-2]`.

Сложность:
- время: **O(n)**;
- память: **O(1)**, если хранить только два предыдущих состояния.

Термины: **recurrence**, **state compression**, **base cases**.

```go
package main

func climbStairs(n int) int {
	if n <= 2 {
		return n // База: 1 -> 1, 2 -> 2.
	}

	prev2, prev1 := 1, 2 // dp[i-2], dp[i-1]
	for i := 3; i <= n; i++ {
		cur := prev1 + prev2 // Текущее число способов.
		prev2 = prev1
		prev1 = cur
	}

	return prev1
}
```

> “I use a Fibonacci-style recurrence and compress state to two scalars for constant auxiliary memory.”

- [Climbing Stairs на LeetCode](https://leetcode.com/problems/climbing-stairs/)
- [Оглавление книги](./README.md)
