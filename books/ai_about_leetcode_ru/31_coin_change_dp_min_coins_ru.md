# 31. Coin Change: минимум монет через DP без самообмана

Задача коварная: локально «крупная монета лучше» звучит разумно, но жадность здесь может провалиться. Нужен системный учёт всех вариантов.

Идея:
- `dp[x]` — минимум монет для суммы `x`;
- инициализируем `dp[0] = 0`, остальное как «бесконечность»;
- для каждой суммы пробуем все номиналы;
- берём лучший переход `dp[x - coin] + 1`.

Сложность:
- время: **O(amount × k)**, где `k` — число номиналов;
- память: **O(amount)**.

Термины:
- **state transition** — переход между состояниями DP;
- **sentinel infinity** — маркер недостижимого состояния;
- **unbounded knapsack pattern** — шаблон с неограниченным числом элементов.

Пример на Go:

```go
package main

func coinChange(coins []int, amount int) int {
    const INF = int(1e9)
    dp := make([]int, amount+1)

    for i := 1; i <= amount; i++ {
        dp[i] = INF
    }

    for x := 1; x <= amount; x++ {
        for _, c := range coins {
            if c <= x && dp[x-c] != INF {
                if dp[x-c]+1 < dp[x] {
                    dp[x] = dp[x-c] + 1
                }
            }
        }
    }

    if dp[amount] == INF {
        return -1
    }
    return dp[amount]
}
```

Интервью-ответ:

> “I use bottom-up DP where each amount keeps the minimum number of coins needed. Every coin is a candidate transition, and unreachable states stay marked as infinity.”  
> [«Я использую bottom-up DP, где для каждой суммы хранится минимальное число монет. Каждая монета — кандидат на переход, а недостижимые состояния остаются помечены как бесконечность».]

Фразы для фиксации:
- “Greedy feels right. DP proves right.”  
  [«Жадность звучит правдоподобно. DP доказывает корректность».]
- “Unreachable is data, not an error.”  
  [«Недостижимость — это данные, а не ошибка».]

Рабочая аналогия: минимальная стоимость набора ресурсов, оптимальный набор купонов, подбор пакетов тарифа под целевой объём.

Отличный момент прогресса: вы уже не спорите с задачей «интуицией». Вы строите модель, которая выдерживает проверку на крайних кейсах.

Полезные ссылки:
- [Coin Change на LeetCode](https://leetcode.com/problems/coin-change/)
- [Глава про Pacific Atlantic Water Flow](./30_pacific_atlantic_reverse_flow_ru.md)
- [Оглавление книги](./README.md)
