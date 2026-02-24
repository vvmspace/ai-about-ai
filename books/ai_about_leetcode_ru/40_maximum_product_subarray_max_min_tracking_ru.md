# 40. Maximum Product Subarray: максимум и минимум одновременно

Вот где интервью обычно становится тише: отрицательные числа ломают интуицию, и «просто хранить максимум» уже не работает.

Почему задача коварна:
- отрицательное число может превратить минимальный продукт в новый максимум;
- ноль обнуляет текущее состояние и создаёт естественную границу сегмента;
- ответ может появиться внезапно после «плохого» префикса.

Надёжная модель:
- `cur_max` — лучший продукт, оканчивающийся в текущей позиции;
- `cur_min` — худший (самый маленький) продукт, оканчивающийся в текущей позиции;
- при каждом `x` пересчитываем оба через тройку кандидатов: `x`, `x * cur_max_old`, `x * cur_min_old`.

Сложность:
- время: **O(n)**;
- память: **O(1)**.

Термины:
- **sign flip effect** — эффект смены знака;
- **state pair tracking** — отслеживание пары состояний;
- **segment reset by zero** — сброс сегмента нулём.

Пример на Python:

```python
from typing import List


def maxProduct(nums: List[int]) -> int:
    cur_max = nums[0]
    cur_min = nums[0]
    ans = nums[0]

    for x in nums[1:]:
        prev_max, prev_min = cur_max, cur_min
        cur_max = max(x, x * prev_max, x * prev_min)
        cur_min = min(x, x * prev_max, x * prev_min)
        ans = max(ans, cur_max)

    return ans
```

Пример ответа на интервью:

> “For product subarrays I track both extremes at each index, because a negative value can swap roles: yesterday’s minimum can become today’s maximum.”  
> [«Для product subarray я храню оба экстремума на каждом индексе, потому что отрицательное значение меняет роли: вчерашний минимум может стать сегодняшним максимумом».]

Пара фраз для памяти:
- “Track both edges of the state.”  
  [«Держи обе границы состояния».]
- “Negative numbers reverse power.”  
  [«Отрицательные числа меняют расклад сил».]

Где это в работе: анализ мультипликативных рисков, модели изменения метрик в процентах, расчёт эффекта цепочек коэффициентов в финтехе.

Вы только что приручили задачу, в которой большинство делает неверную редукцию. Это не просто плюс к алгоритмам — это плюс к инженерной внимательности.

Полезные ссылки:
- [Maximum Product Subarray на LeetCode](https://leetcode.com/problems/maximum-product-subarray/)
- [Глава про Gas Station](./39_gas_station_circular_balance_ru.md)
- [Оглавление книги](./README.md)
