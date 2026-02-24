# 38. Jump Game: жадность и достижимость

На этой задаче многие теряют уверенность неожиданно быстро: массив маленький, а ощущение, будто нужен динамический монстр. Не нужен.

Идея строгая и спокойная:
- держим `farthest` — самую дальнюю достижимую позицию;
- идём слева направо;
- если `i > farthest`, мы уже упёрлись в недостижимую точку;
- иначе расширяем горизонт: `farthest = max(farthest, i + nums[i])`.

Почему это работает:
- нам не важно, **как именно** пришли в позицию, важно только, можем ли прийти вообще;
- `farthest` — полный срез этого знания на текущем шаге;
- как только горизонт покрывает последний индекс, задачу можно считать закрытой.

Сложность:
- время: **O(n)**;
- память: **O(1)**.

Термины:
- **reachability frontier** — фронтир достижимости;
- **greedy invariant** — инвариант жадного алгоритма;
- **early termination** — досрочное завершение.

Пример на JavaScript:

```javascript
function canJump(nums) {
  let farthest = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i > farthest) return false;
    farthest = Math.max(farthest, i + nums[i]);
    if (farthest >= nums.length - 1) return true;
  }

  return true;
}
```

Пример ответа на интервью:

> “I track the farthest reachable index while scanning once. If the current index is beyond that frontier, the game is over; otherwise I keep expanding the frontier greedily.”  
> [«Я отслеживаю самый дальний достижимый индекс за один проход. Если текущий индекс за пределом фронтира, игра закончена; иначе жадно расширяю фронтир».]

Пара фраз для памяти:
- “Reachability first. Path later.”  
  [«Сначала достижимость. Путь — потом».]
- “If the frontier dies, the solution dies.”  
  [«Если фронтир умер, решение умерло».]

Где это встречается в работе: проверка достижимости этапов в workflow, контроль прогресса пользователя по сценариям, анализ «доживёт ли задача до финального статуса» в очередях.

Хорошая новость проста: вы только что закрыли задачу, которая пугает внешне и решается одной переменной. Это сильный психологический буст перед следующими главами.

Полезные ссылки:
- [Jump Game на LeetCode](https://leetcode.com/problems/jump-game/)
- [Глава про Unique Paths](./37_unique_paths_combinatorics_and_dynamic_programming_ru.md)
- [Оглавление книги](./README.md)
