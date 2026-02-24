# 32. Combination Sum: backtracking, который не уходит в хаос

На первый взгляд это просто перебор. В реальности интервьюер проверяет, умеете ли вы держать дерево решений под контролем и отсекать лишнее заранее.

Модель:
- строим комбинацию постепенно;
- можно брать текущий кандидат повторно;
- переходим к следующему только когда решаем «не брать»;
- останавливаем ветку, если сумма уже превысила цель.

Сложность:
- время: экспоненциальное в худшем случае;
- память: **O(target)** на глубину рекурсии и путь.

Термины:
- **search tree** — дерево вариантов решения;
- **pruning** — отсечение ветвей, которые не приведут к ответу;
- **path state** — текущее состояние частичного решения.

Пример на JavaScript:

```javascript
function combinationSum(candidates, target) {
  const result = [];
  const path = [];

  function dfs(start, remain) {
    if (remain === 0) {
      result.push([...path]);
      return;
    }
    if (remain < 0) return;

    for (let i = start; i < candidates.length; i++) {
      const val = candidates[i];
      path.push(val);
      dfs(i, remain - val); // можно использовать тот же элемент снова
      path.pop();
    }
  }

  dfs(0, target);
  return result;
}
```

Интервью-ответ:

> “I run depth-first backtracking with a non-decreasing index, so combinations are generated without permutation duplicates. Branches with negative remainder are pruned immediately.”  
> [«Я запускаю backtracking в глубину с неубывающим индексом, поэтому комбинации генерируются без дубликатов-перестановок. Ветки с отрицательным остатком отсекаются сразу».]

Фразы, которые хорошо держатся в памяти:
- “Build. Check. Roll back.”  
  [«Построй. Проверь. Откати».]
- “Pruning is performance with discipline.”  
  [«Отсечения — это производительность через дисциплину».]

Где это в работе: генерация конфигураций, подбор набора фич под бюджет, поиск допустимых комбинаций параметров в планировщике.

Вы уже чувствуете контроль: backtracking перестал быть «магией рекурсии» и стал прозрачным процессом с понятными инвариантами.

Полезные ссылки:
- [Combination Sum на LeetCode](https://leetcode.com/problems/combination-sum/)
- [Глава про Coin Change](./31_coin_change_dp_min_coins_ru.md)
- [Оглавление книги](./README.md)
