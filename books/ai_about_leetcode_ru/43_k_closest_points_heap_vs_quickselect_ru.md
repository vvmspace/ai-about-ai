# 43. K Closest Points to Origin: quickselect против heap

Здесь вас проверяют не на формулу расстояния, а на инженерный выбор алгоритма под ограничения. Формула тривиальна. Выбор — нет.

Есть два рабочих подхода:
- `max-heap` размера `k`: стабильно и понятно;
- `quickselect`: в среднем быстрее на больших данных, но сложнее в реализации.

Практический ориентир:
- если нужен поток или данные приходят постепенно — берите heap;
- если массив фиксирован и важна средняя линейная скорость — quickselect;
- на интервью обычно безопасно начать с heap, затем коротко обсудить quickselect.

Сложность:
- heap: время **O(n log k)**, память **O(k)**;
- quickselect: среднее время **O(n)**, худшее **O(n²)**, память **O(1)** (in-place).

Термины:
- **selection algorithm** — алгоритм выбора k-го порядка;
- **partial order maintenance** — поддержание частичного порядка;
- **average-case optimisation** — оптимизация в среднем случае.

Пример на Go (heap):

```go
package main

import "container/heap"

type Point struct {
    x, y int
}

type MaxHeap []Point

func (h MaxHeap) Len() int { return len(h) }
func (h MaxHeap) Less(i, j int) bool {
    return h[i].x*h[i].x+h[i].y*h[i].y > h[j].x*h[j].x+h[j].y*h[j].y
}
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(v interface{}) { *h = append(*h, v.(Point)) }
func (h *MaxHeap) Pop() interface{} {
    old := *h
    n := len(old)
    item := old[n-1]
    *h = old[:n-1]
    return item
}

func kClosest(points [][]int, k int) [][]int {
    h := &MaxHeap{}
    heap.Init(h)

    for _, p := range points {
        heap.Push(h, Point{p[0], p[1]})
        if h.Len() > k {
            heap.Pop(h)
        }
    }

    ans := make([][]int, 0, k)
    for h.Len() > 0 {
        p := heap.Pop(h).(Point)
        ans = append(ans, []int{p.x, p.y})
    }
    return ans
}
```

Пример ответа на интервью:

> “I pick max-heap of size k for predictable O(n log k) behaviour; then I mention quickselect as an average O(n) alternative when in-place partitioning is acceptable.”  
> [«Я выбираю max-heap размера k ради предсказуемого поведения O(n log k); затем упоминаю quickselect как альтернативу со средним O(n), если допустимо in-place разбиение».]

Пара фраз для памяти:
- “Pick the model, not the myth.”  
  [«Выбирай модель, а не миф».]
- “Predictability often wins interviews.”  
  [«Предсказуемость часто выигрывает интервью».]

Где это в работе: top-k рекомендаций, ближайшие объекты на карте, отбор лучших кандидатов по скоринговой метрике.

Отличный сдвиг мышления: вы обсуждаете не только «что работает», но и «что устойчиво под реальные ограничения».

Полезные ссылки:
- [K Closest Points to Origin на LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/)
- [Глава про Rotting Oranges](./42_rotting_oranges_bfs_time_layers_ru.md)
- [Оглавление книги](./README.md)
