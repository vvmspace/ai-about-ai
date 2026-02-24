# 35. House Robber: выбор с конфликтом соседей через динамическое программирование

Задача звучит почти как шутка, но проверяет очень серьёзный навык: умеете ли вы принимать решение, когда локальная выгода конфликтует с соседним шагом.

Модель dynamic programming (динамическое программирование):
- `dp[i]` — максимум денег на префиксе до дома `i`;
- для каждого дома есть два варианта: взять текущий дом или пропустить;
- переход: `dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])`.

Сложность:
- время: **O(n)**;
- память: **O(1)**, если хранить только два предыдущих состояния.

Термины:
- **mutual exclusion** — взаимоисключение соседних выборов;
- **rolling state** — скользящее хранение ограниченного числа состояний;
- **optimal substructure** — оптимальность решения через оптимальные подзадачи.

Пример на JavaScript:

```javascript
function rob(nums) {
  let prevTwo = 0; // значение для позиции i - 2
  let prevOne = 0; // значение для позиции i - 1

  for (const money of nums) {
    const take = prevTwo + money;
    const skip = prevOne;
    const current = Math.max(take, skip);

    prevTwo = prevOne;
    prevOne = current;
  }

  return prevOne;
}
```

Интервью-ответ:

> “At each house I compare two legal states: skip current and keep previous best, or take current and add the best from two steps back. This yields linear time with constant memory.”  
> [«На каждом доме я сравниваю два допустимых состояния: пропустить текущий и оставить прошлый максимум, либо взять текущий и прибавить максимум двух шагов назад. Это даёт линейное время и константную память».]

Фразы для запоминания:
- “Take or skip. Nothing else.”  
  [«Взять или пропустить. Третьего не дано».]
- “Local conflict, global optimum.”  
  [«Локальный конфликт, глобальный оптимум».]

Где это встречается в работе: выбор независимых задач в расписании, распределение бюджета по взаимоисключающим инициативам, оптимизация промо-слотов при ограничениях соседства.

Хорошая новость: это уже уровень, где вы не просто пишете код, а умеете спокойно объяснить, почему решение устойчиво на длинных входах.

Полезные ссылки:
- [House Robber на LeetCode](https://leetcode.com/problems/house-robber/)
- [Глава про Longest Increasing Subsequence](./34_longest_increasing_subsequence_quadratic_and_binary_search_ru.md)
- [Оглавление книги](./README.md)
