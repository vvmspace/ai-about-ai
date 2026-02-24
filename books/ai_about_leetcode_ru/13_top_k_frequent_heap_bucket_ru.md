# 13. Top K Frequent Elements: выбор через bounded heap

Здесь главное — отделить две фазы: посчитать частоты и выбрать top-K. Если `k` заметно меньше `n`, min-heap размера `k` даёт аккуратный баланс.

Сложность:
- время: **O(n log k)**;
- память: **O(n)**.

Термины: **frequency map**, **bounded heap**, **selection pipeline**.

```python
import heapq

def top_k_frequent(nums, k):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1  # Шаг 1: считаем частоты.

    heap = []
    for val, cnt in freq.items():
        heapq.heappush(heap, (cnt, val))   # Держим кандидатов в min-heap.
        if len(heap) > k:
            heapq.heappop(heap)             # Удаляем наименее частый.

    return [val for _, val in heap]
```

> “I keep only K best frequency candidates in a bounded min-heap, which gives O(n log k) selection cost.”

- [Top K Frequent Elements на LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)
- [Оглавление книги](./README.md)
