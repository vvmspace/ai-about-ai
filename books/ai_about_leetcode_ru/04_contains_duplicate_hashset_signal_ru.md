# 04. Contains Duplicate: хеш-таблица как фильтр шума

Задача простая только снаружи. Внутри она про архитектурное мышление: как быстро понять, нарушена ли уникальность потока.

Если идти «в лоб», можно сравнить каждую пару и получить O(n²). Но в инженерной практике мы почти всегда используем структуру членства — `set`.

Идея элементарна:
- создаём пустой `set`;
- идём по элементам;
- если элемент уже в `set`, сразу возвращаем `true`;
- иначе добавляем и продолжаем.

Сложность:
- время: **O(n)** в среднем;
- память: **O(n)**.

Неочевидные термины:
- **membership query** — проверка «принадлежит ли элемент множеству»;
- **cardinality** — мощность множества (число уникальных элементов);
- **short-circuit evaluation** — раннее завершение при первом доказательстве ответа.

Пример на JavaScript:

```javascript
function containsDuplicate(nums) {
  const seen = new Set(); // Храним только уникальные значения.

  for (const x of nums) {
    // Membership query: уже встречали элемент?
    if (seen.has(x)) {
      return true; // Short-circuit: дубликат найден.
    }

    seen.add(x); // Добавляем новое уникальное значение.
  }

  return false; // Все элементы были уникальны.
}
```

Пример на Go:

```go
package main

func containsDuplicate(nums []int) bool {
	seen := make(map[int]struct{}, len(nums)) // struct{} минимизирует накладные расходы.

	for _, x := range nums {
		if _, exists := seen[x]; exists {
			return true // Ранний выход при первом дубликате.
		}
		seen[x] = struct{}{}
	}

	return false
}
```

Интервью-ответ:

> “I use a hash-based membership structure and short-circuit on first repetition. That converts pairwise comparison into linear scan with expected constant-time lookups.”  
> [«Я использую хеш-структуру для membership-проверок и завершаю алгоритм при первом повторе. Это заменяет попарные сравнения на линейный проход с ожидаемым константным доступом».]

Пара фраз:
- “Uniqueness is a set problem.”  
  [«Уникальность — это задача множества».]
- “I optimise for first evidence, not full traversal.”  
  [«Я оптимизируюсь под первое доказательство, а не под полный проход».]

В работе это встречается постоянно: дедупликация event stream, защита от повторной обработки webhook, контроль idempotency key, фильтрация повторов в ETL-пайплайнах.

Маленькая награда за дисциплину: вы уже прошли четыре ключевых паттерна подряд — hash map, stack, pointer merge и set membership. Это ровно тот фундамент, на котором собеседования становятся предсказуемыми, а не нервными.

Полезные ссылки:
- [Contains Duplicate на LeetCode](https://leetcode.com/problems/contains-duplicate/)
- [Оглавление книги](./README.md)
