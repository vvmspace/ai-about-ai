# 50. Edit Distance: цена преобразования строки

Финальная глава намеренно строгая. Здесь важно показать, что вы управляете моделью преобразований, а не импровизируете по месту.

Модель Levenshtein distance:
- `dp[i][j]` — минимальное число операций, чтобы превратить `word1[:i]` в `word2[:j]`;
- операции: вставка, удаление, замена;
- если символы равны, берём диагональ без доплаты.

Переход:
- если `word1[i-1] == word2[j-1]`, `dp[i][j] = dp[i-1][j-1]`;
- иначе `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`.

Сложность:
- время: **O(m × n)**;
- память: **O(m × n)**, можно сжать до **O(n)**.

Термины:
- **operation cost model** — модель стоимости операций;
- **alignment matrix** — матрица выравнивания;
- **optimal substructure** — оптимальная подструктура.

Пример на Rust:

```rust
pub fn min_distance(word1: String, word2: String) -> i32 {
    let a: Vec<char> = word1.chars().collect();
    let b: Vec<char> = word2.chars().collect();
    let m = a.len();
    let n = b.len();

    let mut dp = vec![vec![0i32; n + 1]; m + 1];
    for i in 0..=m { dp[i][0] = i as i32; }
    for j in 0..=n { dp[0][j] = j as i32; }

    for i in 1..=m {
        for j in 1..=n {
            if a[i - 1] == b[j - 1] {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + dp[i - 1][j].min(dp[i][j - 1]).min(dp[i - 1][j - 1]);
            }
        }
    }

    dp[m][n]
}
```

Пример ответа на интервью:

> “I define DP over string prefixes where each cell is the minimum edit cost. Transitions represent insert, delete, replace, and matching characters reuse diagonal state.”  
> [«Я задаю DP по префиксам строк, где каждая ячейка — минимальная цена редактирования. Переходы соответствуют insert, delete, replace, а совпадение символов использует диагональное состояние».]

Пара фраз для памяти:
- “Model the cost, then optimise.”  
  [«Сначала смоделируй стоимость, потом оптимизируй».]
- “DP turns ambiguity into certainty.”  
  [«DP превращает неопределённость в определённость».]

Где это в работе: дедупликация текстов, quality-контроль ввода, сравнение версий строковых конфигураций.

Сильное завершение книги: вы прошли от базовых паттернов к задаче, где ценится точность мышления и спокойная формализация.

Полезные ссылки:
- [Edit Distance на LeetCode](https://leetcode.com/problems/edit-distance/)
- [Глава про Alien Dictionary](./49_alien_dictionary_topological_order_ru.md)
- [Оглавление книги](./README.md)
