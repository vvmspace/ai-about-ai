# 13. Top K Frequent Elements: куча и bucket-подход

Сначала считаем частоты, потом выбираем top-K. Чаще всего — min-heap размера `k`.

Сложность heap-решения:
- время: **O(n log k)**;
- память: **O(n)**.

Термины: **frequency map**, **bounded heap**, **selection under constraint**.

```python
import heapq

def top_k_frequent(nums, k):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    heap = []
    for val, count in freq.items():
        heapq.heappush(heap, (count, val))
        if len(heap) > k:
            heapq.heappop(heap)

    return [val for _, val in heap]
```

> “I use a bounded min-heap to keep only K best candidates while scanning frequency counts.”

- [Top K Frequent Elements на LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)
- [Оглавление книги](./README.md)
