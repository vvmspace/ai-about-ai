# 46. Median of Two Sorted Arrays: бинарный поиск по разбиению

Эта задача обычно производит нужный эффект: формулировка короткая, а цена ошибки в логике высокая. Именно поэтому она так любима на интервью.

Главная идея:
- делим два отсортированных массива на левую и правую части;
- в левой части должно быть ровно половина элементов;
- все элементы слева должны быть `<=` всем элементам справа.

Трюк в том, что ищем не саму медиану, а корректную позицию разреза в меньшем массиве через binary search.

Сложность:
- время: **O(log(min(m, n)))**;
- память: **O(1)**.

Термины:
- **partition boundary** — граница разбиения;
- **balanced split** — сбалансированный разрез;
- **order constraint** — ограничение порядка.

Пример на Python:

```python
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    a, b = nums1, nums2
    if len(a) > len(b):
        a, b = b, a

    total = len(a) + len(b)
    half = total // 2
    left, right = 0, len(a)

    while True:
        i = (left + right) // 2
        j = half - i

        a_left = a[i - 1] if i > 0 else float("-inf")
        a_right = a[i] if i < len(a) else float("inf")
        b_left = b[j - 1] if j > 0 else float("-inf")
        b_right = b[j] if j < len(b) else float("inf")

        if a_left <= b_right and b_left <= a_right:
            if total % 2:
                return min(a_right, b_right)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            right = i - 1
        else:
            left = i + 1
```

Пример ответа на интервью:

> “I do binary search on partition index in the smaller array and enforce ordering across partition borders. Once the border is valid, median is immediate.”  
> [«Я делаю бинарный поиск по индексу разбиения в меньшем массиве и соблюдаю порядок на границах разбиения. Как только граница валидна, медиана вычисляется сразу».]

Пара фраз для памяти:
- “Search the cut, not the value.”  
  [«Ищи разрез, а не значение».]
- “Partition validity gives the answer.”  
  [«Валидность разбиения даёт ответ».]

Где это в работе: объединение отсортированных потоков метрик, аналитика по percentile, расчёт центральных значений в больших наборах.

Полезные ссылки:
- [Median of Two Sorted Arrays на LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- [Глава про LRU Cache](./45_lru_cache_hashmap_doubly_linked_list_ru.md)
- [Оглавление книги](./README.md)
