# 47. Regular Expression Matching: строгое динамическое программирование

Эта глава важна не из-за синтаксиса regex. Важна дисциплина формализации: что именно означает `dp[i][j]`, и как аккуратно обрабатывать `.` и `*`.

Модель:
- `dp[i][j]` — совпадает ли `s[:i]` с `p[:j]`;
- `.` совпадает с любым одним символом;
- `*` работает только вместе с предыдущим символом и даёт два варианта: взять ноль раз или один/больше.

Переходы:
- обычный символ или `.`: `dp[i][j] = dp[i-1][j-1]` при совпадении;
- `*`: `dp[i][j] = dp[i][j-2]` (ноль вхождений) или, если текущий символ подходит, `dp[i-1][j]`.

Сложность:
- время: **O(m × n)**;
- память: **O(m × n)**.

Термины:
- **state matrix** — матрица состояний;
- **zero-occurrence branch** — ветка нулевого вхождения;
- **carry-over match** — перенос совпадения по строке.

Пример на JavaScript:

```javascript
function isMatch(s, p) {
  const m = s.length, n = p.length;
  const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(false));
  dp[0][0] = true;

  for (let j = 2; j <= n; j++) {
    if (p[j - 1] === '*') dp[0][j] = dp[0][j - 2];
  }

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (p[j - 1] === '.' || p[j - 1] === s[i - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else if (p[j - 1] === '*') {
        dp[i][j] = dp[i][j - 2];
        const prev = p[j - 2];
        if (prev === '.' || prev === s[i - 1]) dp[i][j] = dp[i][j] || dp[i - 1][j];
      }
    }
  }

  return dp[m][n];
}
```

Пример ответа на интервью:

> “I use DP over string and pattern prefixes. For `*`, I split logic into zero occurrences and repeated occurrences of the previous token.”  
> [«Я использую DP по префиксам строки и паттерна. Для `*` разделяю логику на ноль вхождений и повтор предыдущего токена».]

Пара фраз для памяти:
- “Define state first, code second.”  
  [«Сначала определи состояние, потом код».]
- “`*` means two branches, always.”  
  [«`*` всегда означает две ветки».]

Где это в работе: валидация правил фильтрации, сопоставление шаблонов в логах, проверка форматных ограничений в ETL.

Полезные ссылки:
- [Regular Expression Matching на LeetCode](https://leetcode.com/problems/regular-expression-matching/)
- [Глава про Median of Two Sorted Arrays](./46_median_of_two_sorted_arrays_partition_binary_search_ru.md)
- [Оглавление книги](./README.md)
