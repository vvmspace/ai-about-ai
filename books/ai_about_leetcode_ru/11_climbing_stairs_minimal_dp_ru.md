# 11. Climbing Stairs: минимальная динамика без тумана

Здесь любят ловить на рекурсии. Кандидат пишет красивый код, а затем спокойно получает экспоненту по времени.

Модель простая: чтобы попасть на ступень `i`, вы приходите либо с `i-1`, либо с `i-2`.
Значит:
`dp[i] = dp[i-1] + dp[i-2]`.

Это буквально Фибоначчи в инженерной упаковке.

Сложность с оптимизацией памяти:
- время: **O(n)**;
- память: **O(1)**.

Неочевидные термины:
- **state transition** — правило перехода между состояниями DP;
- **overlapping subproblems** — повторяющиеся подзадачи, из-за которых рекурсия тормозит;
- **tabulation** — построение ответа снизу вверх.

Пример на Go:

```go
package main

func climbStairs(n int) int {
	if n <= 2 {
		return n
	}

	prev2, prev1 := 1, 2
	for i := 3; i <= n; i++ {
		curr := prev1 + prev2
		prev2 = prev1
		prev1 = curr
	}

	return prev1
}
```

Интервью-ответ:

> “This is a one-dimensional dynamic programming problem with two-term recurrence. I keep only the last two states, so the solution remains linear in time and constant in extra memory.”  
> [«Это одномерная задача динамического программирования с рекуррентой из двух слагаемых. Я храню только два последних состояния, поэтому решение остаётся линейным по времени и константным по дополнительной памяти».]

Пара фраз:
- “DP is just controlled memory of decisions.”  
  [«DP — это просто управляемая память о решениях».]
- “If recurrence is clear, implementation is routine.”  
  [«Если рекуррента ясна, реализация становится рутиной».]

Где это в работе: подсчёт числа маршрутов в навигации, моделей отказоустойчивых путей, оценка количества допустимых сценариев в бизнес-правилах.

Полезные ссылки:
- [Climbing Stairs на LeetCode](https://leetcode.com/problems/climbing-stairs/)
- [Глава про Maximum Subarray](./05_maximum_subarray_kadane_signal_ru.md)
- [Оглавление книги](./README.md)
