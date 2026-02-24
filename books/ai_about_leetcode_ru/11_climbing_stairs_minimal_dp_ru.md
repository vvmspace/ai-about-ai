# 11. Climbing Stairs: минимальная динамика

Это чистый вход в DP: чтобы попасть на ступень `i`, мы приходим с `i-1` или `i-2`. Значит, `dp[i] = dp[i-1] + dp[i-2]`.

Сложность:
- время: **O(n)**;
- память: **O(1)** через компрессию состояния.

Термины: **recurrence relation**, **state compression**, **base cases**.

```go
package main

func climbStairs(n int) int {
	if n <= 2 {
		return n
	}
	prev2, prev1 := 1, 2 // dp[i-2], dp[i-1]
	for i := 3; i <= n; i++ {
		cur := prev1 + prev2
		prev2 = prev1
		prev1 = cur
	}
	return prev1
}
```

> “I model it as a Fibonacci-style recurrence and compress DP state to two scalars for constant auxiliary memory.”

- [Climbing Stairs на LeetCode](https://leetcode.com/problems/climbing-stairs/)
- [Оглавление книги](./README.md)
