# 19. Ransom Note: частотный бюджет без паники

Задача короткая, но очень показательная: умеете ли вы мыслить ресурсами, а не символами.

Модель простая:
- `magazine` — это склад букв;
- `ransomNote` — это спрос;
- если спрос по любой букве превышает запас, ответ сразу `false`.

Сложность:
- время: **O(m + n)**;
- память: **O(1)** для фиксированного алфавита (или O(k) в общем случае).

Неочевидные термины:
- **frequency budget** — доступный лимит по каждому символу;
- **deficit detection** — раннее обнаружение нехватки ресурса;
- **constant alphabet bound** — ограниченность памяти размером алфавита.

Пример на Go:

```go
package main

func canConstruct(ransomNote string, magazine string) bool {
	count := make([]int, 26)

	for _, ch := range magazine {
		count[ch-'a']++
	}

	for _, ch := range ransomNote {
		idx := ch - 'a'
		count[idx]--
		if count[idx] < 0 {
			return false
		}
	}

	return true
}
```

Интервью-ответ:

> “I treat magazine letters as inventory and the note as demand. A frequency array gives linear time, and any negative counter immediately proves infeasibility.”  
> [«Я рассматриваю буквы magazine как склад, а записку как спрос. Массив частот даёт линейное время, и любой отрицательный счётчик сразу доказывает невозможность».]

Пара фраз:
- “No inventory, no output.”  
  [«Нет запаса — нет результата».]
- “Negative count means hard stop.”  
  [«Отрицательный счётчик — немедленная остановка».]

Где это в работе: проверка квот API, контроль остатков в корзине, валидация лимитов на отправку уведомлений.

Полезные ссылки:
- [Ransom Note на LeetCode](https://leetcode.com/problems/ransom-note/)
- [Глава про Valid Anagram](./07_valid_anagram_frequency_models_ru.md)
- [Оглавление книги](./README.md)
