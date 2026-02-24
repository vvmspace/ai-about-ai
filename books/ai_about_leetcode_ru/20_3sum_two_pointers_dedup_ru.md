# 20. 3Sum: сортировка, два указателя и контроль дублей

Вот здесь многие резко теряют темп. Кажется, что нужно «что-то хитрое», хотя ядро задачи предельно инженерное: порядок, указатели, дисциплина.

Алгоритм:
- сортируем массив;
- фиксируем индекс `i`;
- для остатка используем два указателя `left/right`;
- после найденной тройки аккуратно пропускаем дубли.

Сложность:
- время: **O(n²)**;
- память: **O(1)** без учёта результата.

Неочевидные термины:
- **duplicate skipping policy** — правило пропуска повторов, чтобы не плодить одинаковые тройки;
- **search window contraction** — сужение интервала указателями в зависимости от суммы;
- **sorted constraint leverage** — использование отсортированности для линейного шага внутри цикла.

Пример на JavaScript:

```javascript
function threeSum(nums) {
  nums.sort((a, b) => a - b);
  const result = [];

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum < 0) left++;
      else if (sum > 0) right--;
      else {
        result.push([nums[i], nums[left], nums[right]]);
        left++;
        right--;

        while (left < right && nums[left] === nums[left - 1]) left++;
        while (left < right && nums[right] === nums[right + 1]) right--;
      }
    }
  }

  return result;
}
```

Интервью-ответ:

> “I sort first, then reduce 3Sum to repeated 2Sum with two pointers. The critical part is deterministic duplicate handling, otherwise correctness is incomplete.”  
> [«Я сначала сортирую, затем свожу 3Sum к повторяющемуся 2Sum с двумя указателями. Критическая часть — детерминированная обработка дублей, иначе корректность неполная».]

Пара фраз:
- “Sort once, reason clearly.”  
  [«Один раз отсортируй — дальше рассуждай чисто».]
- “Duplicates are a correctness problem, not cosmetics.”  
  [«Дубли — это проблема корректности, а не косметика».]

Где это в работе: поиск сбалансированных комбинаций скидок, подбор триад параметров с нулевым балансом отклонений, анализ взаимных компенсаций в финансовых потоках.

Двадцатая глава — это дофаминовый момент: вы уже не решаете задачи поштучно, вы видите паттерны, а это именно то состояние, когда интервью начинает работать на вас.

Полезные ссылки:
- [3Sum на LeetCode](https://leetcode.com/problems/3sum/)
- [Глава про Two Sum](./00_two_sum_the_most_famous_start_ru.md)
- [Оглавление книги](./README.md)
