# 33. Word Break: границы строки и DP-проверка выполнимости

Проблема выглядит как «угадай разбиение». Но по сути это вопрос выполнимости: можно ли дойти до конца строки, если допустимы только слова из словаря.

Идея:
- `dp[i] = true`, если префикс `s[0:i]` разбивается на словарные слова;
- стартуем с `dp[0] = true`;
- для каждого `i` ищем `j < i`, где `dp[j] = true` и `s[j:i]` есть в словаре;
- если нашли, отмечаем `dp[i] = true`.

Сложность:
- время: **O(n²)** проверок подстрок (без дополнительных оптимизаций);
- память: **O(n)**.

Термины:
- **prefix feasibility** — выполнимость префикса;
- **dictionary lookup** — проверка принадлежности словарю;
- **boolean DP** — динамика с true/false-состояниями.

Пример на Rust:

```rust
use std::collections::HashSet;

pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
    let set: HashSet<String> = word_dict.into_iter().collect();
    let chars: Vec<char> = s.chars().collect();
    let n = chars.len();
    let mut dp = vec![false; n + 1];
    dp[0] = true;

    for i in 1..=n {
        for j in 0..i {
            if !dp[j] {
                continue;
            }
            let part: String = chars[j..i].iter().collect();
            if set.contains(&part) {
                dp[i] = true;
                break;
            }
        }
    }

    dp[n]
}
```

Интервью-ответ:

> “I model this as prefix feasibility with boolean DP. If any valid previous cut plus dictionary lookup reaches index i, then i is feasible.”  
> [«Я моделирую задачу как выполнимость префиксов через boolean DP. Если любой валидный предыдущий разрез плюс проверка словаря достигают индекса i, значит i выполним».]

Фразы для закрепления:
- “Cut points are states.”  
  [«Точки разреза — это состояния».]
- “If prefixes work, the whole string works.”  
  [«Если работают префиксы, сработает и вся строка».]

Где это в проде: токенизация и валидация пользовательского ввода, проверка составных кодов, разбор доменных строк по словарю допустимых сегментов.

И да, это очень приятный рубеж: вы научились видеть в строках не хаос символов, а чёткие состояния и переходы. На интервью это считывается мгновенно.

Полезные ссылки:
- [Word Break на LeetCode](https://leetcode.com/problems/word-break/)
- [Глава про Combination Sum](./32_combination_sum_backtracking_cuts_ru.md)
- [Оглавление книги](./README.md)
