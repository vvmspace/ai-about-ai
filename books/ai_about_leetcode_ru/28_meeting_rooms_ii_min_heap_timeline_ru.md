# 28. Meeting Rooms II: минимальное число комнат как контроль пиков

Если коротко, это не про переговорки. Это про пиковую нагрузку во времени. Сколько параллельных «юнитов ресурса» вам нужно в худший момент.

Подход:
- сортируем встречи по времени начала;
- держим min-heap по времени окончания активных встреч;
- если следующая встреча начинается после минимального конца, комнату переиспользуем;
- иначе добавляем новую комнату.

Сложность:
- время: **O(n log n)**;
- память: **O(n)** в худшем случае.

Термины:
- **active set** — встречи, которые ещё не завершились;
- **peak concurrency** — максимальный уровень одновременности;
- **resource reuse** — переиспользование освобождённого ресурса.

Пример на JavaScript:

```javascript
function minMeetingRooms(intervals) {
  if (intervals.length === 0) return 0;

  intervals.sort((a, b) => a[0] - b[0]);

  const heap = []; // простой min-heap по end

  const push = (x) => {
    heap.push(x);
    let i = heap.length - 1;
    while (i > 0) {
      const p = Math.floor((i - 1) / 2);
      if (heap[p] <= heap[i]) break;
      [heap[p], heap[i]] = [heap[i], heap[p]];
      i = p;
    }
  };

  const pop = () => {
    const top = heap[0];
    const last = heap.pop();
    if (heap.length) {
      heap[0] = last;
      let i = 0;
      while (true) {
        let l = i * 2 + 1, r = i * 2 + 2, m = i;
        if (l < heap.length && heap[l] < heap[m]) m = l;
        if (r < heap.length && heap[r] < heap[m]) m = r;
        if (m === i) break;
        [heap[i], heap[m]] = [heap[m], heap[i]];
        i = m;
      }
    }
    return top;
  };

  push(intervals[0][1]);
  for (let i = 1; i < intervals.length; i++) {
    const [start, end] = intervals[i];
    if (heap[0] <= start) pop();
    push(end);
  }

  return heap.length;
}
```

Интервью-ответ:

> “I model each room as an active meeting end-time in a min-heap. The heap size at any moment is current concurrency, and its maximum gives the required number of rooms.”  
> [«Я моделирую каждую комнату как время окончания активной встречи в min-heap. Размер heap в моменте — текущая параллельность, а её максимум даёт нужное число комнат».]

Фразы для закрепления:
- “Track ends, not stories.”  
  [«Следи за концами, а не за историями».]
- “Peaks define capacity.”  
  [«Пики определяют мощность системы».]

Где это в проде: sizing воркеров, лимиты соединений, планирование batch-окон в ETL.

Вы уже на приятной скорости: начинаете видеть за задачей системную метрику. Это даёт тот самый дофаминовый щелчок — «я не угадываю, я моделирую».

Полезные ссылки:
- [Meeting Rooms II на LeetCode](https://leetcode.com/problems/meeting-rooms-ii/)
- [Глава про Non-overlapping Intervals](./27_non_overlapping_intervals_greedy_min_removals_ru.md)
- [Оглавление книги](./README.md)
