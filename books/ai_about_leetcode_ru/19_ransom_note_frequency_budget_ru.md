# 19. Ransom Note: частотный бюджет символов

Суть задачи: есть ли в `magazine` достаточно символов, чтобы собрать `ransomNote`. Это не про строки, это про бюджет частот.

Сложность:
- время: **O(n + m)**;
- память: **O(Σ)**, где `Σ` — размер алфавита.

Термины: **frequency budget**, **deficit detection**, **bounded alphabet optimization**.

```go
package main

func canConstruct(ransomNote string, magazine string) bool {
	cnt := [26]int{}

	for _, ch := range magazine {
		cnt[ch-'a']++ // Пополняем бюджет.
	}

	for _, ch := range ransomNote {
		idx := ch - 'a'
		cnt[idx]--
		if cnt[idx] < 0 {
			return false // Дефицит символа — собрать нельзя.
		}
	}

	return true
}
```

> “I treat magazine letters as a frequency budget and fail fast on first deficit while consuming ransom note characters.”

- [Ransom Note на LeetCode](https://leetcode.com/problems/ransom-note/)
- [Оглавление книги](./README.md)
