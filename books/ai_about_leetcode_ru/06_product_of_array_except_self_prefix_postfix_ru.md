# 06. Product of Array Except Self: префиксы и постфиксы без деления

Эта задача выглядит как арифметика, но на деле она про аккуратную декомпозицию. Деление использовать нельзя. Значит, прямой путь «перемножить всё и поделить» закрыт.

Идея:
- `answer[i]` = произведение всех элементов слева от `i` * произведение всех элементов справа от `i`.
- Сначала проходим слева направо и пишем в `answer[i]` префиксный продукт.
- Потом справа налево домножаем на постфиксный продукт.

Сложность:
- время: **O(n)**;
- память: **O(1)** дополнительная (если не считать выходной массив).

Неочевидные термины:
- **exclusive prefix product** — произведение до позиции, не включая текущий элемент;
- **two-pass accumulation** — накопление в два прохода;
- **numerical robustness** — устойчивость подхода к нулям и знакам без специальных веток «деления».

Пример на JavaScript:

```javascript
function productExceptSelf(nums) {
  const n = nums.length;
  const ans = new Array(n).fill(1);

  let prefix = 1;
  for (let i = 0; i < n; i++) {
    ans[i] = prefix;       // Всё, что слева от i.
    prefix *= nums[i];     // Обновляем префикс для следующей позиции.
  }

  let postfix = 1;
  for (let i = n - 1; i >= 0; i--) {
    ans[i] *= postfix;     // Домножаем на всё, что справа от i.
    postfix *= nums[i];    // Обновляем постфикс.
  }

  return ans;
}
```

Интервью-ответ:

> “I decompose each index result into left and right exclusive products, then compute them with two linear passes. This avoids division, handles zeros naturally, and keeps auxiliary memory constant.”  
> [«Я раскладываю результат для каждого индекса на левое и правое exclusive-произведения, затем считаю их двумя линейными проходами. Это избегает деления, естественно обрабатывает нули и сохраняет константную дополнительную память».]

Пара фраз:
- “Two passes, one invariant per direction.”  
  [«Два прохода, по одному инварианту на каждое направление».]
- “No division, no fragility.”  
  [«Без деления — без хрупкости».]

Где это в работе: вычисление агрегатов «все кроме текущего», метрики влияния одного узла на общий контур, построение фичей для моделей ранжирования.

Полезные ссылки:
- [Product of Array Except Self на LeetCode](https://leetcode.com/problems/product-of-array-except-self/)
- [Оглавление книги](./README.md)
