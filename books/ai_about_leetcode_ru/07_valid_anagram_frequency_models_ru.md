# 07. Valid Anagram: частоты против сортировки

Задача проверяет не знание трюка, а выбор модели. Две строки — анаграммы, если у них одинаковая мультимножество символов.

Есть два пути:
1. Отсортировать обе строки и сравнить.
2. Сравнить частотные словари.

Оба корректны. Но по сложности:
- сортировка: **O(n log n)**;
- частоты: **O(n)**.

Неочевидные термины:
- **multiset equivalence** — эквивалентность мультимножеств;
- **frequency vector** — вектор частот символов;
- **alphabet cardinality bound** — ограниченность алфавита, влияющая на константы.

Пример на Go (частоты):

```go
package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false // Разная длина сразу разрушает эквивалентность.
	}

	freq := make(map[rune]int, len(s))

	for _, ch := range s {
		freq[ch]++ // Увеличиваем частоту для первой строки.
	}

	for _, ch := range t {
		freq[ch]-- // Вычитаем частоту для второй строки.
		if freq[ch] < 0 {
			return false // Символов стало "меньше нуля" — избыток в t.
		}
	}

	return true
}
```

Интервью-ответ:

> “I model each string as a character frequency distribution and compare them in linear time. This avoids sort overhead and scales better when we process many pairs.”  
> [«Я моделирую каждую строку как распределение частот символов и сравниваю их за линейное время. Это избегает накладных расходов сортировки и лучше масштабируется при большом числе пар».]

Пара фраз:
- “Anagram is a multiset question.”  
  [«Анаграмма — это вопрос мультимножества».]
- “I pay O(n), not O(n log n), when counts are enough.”  
  [«Я плачу O(n), а не O(n log n), когда достаточно частот».]

Где это в работе: нормализация поисковых запросов, кластеризация похожих токенов, фильтрация дубликатов по «перестановочному» признаку.

Полезные ссылки:
- [Valid Anagram на LeetCode](https://leetcode.com/problems/valid-anagram/)
- [Оглавление книги](./README.md)
