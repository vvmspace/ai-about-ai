# 19. Ransom Note: частотные словари на практике

Нужно проверить, хватает ли символов `magazine` для сборки `ransomNote`. Это обычная задача на бюджет частот.

Сложность:
- время: **O(n + m)**;
- память: **O(Σ)**, где `Σ` — размер алфавита.

Термины: **frequency budget**, **deficit detection**, **bounded alphabet optimization**.

```go
package main

func canConstruct(ransomNote string, magazine string) bool {
	cnt := [26]int{}
	for _, ch := range magazine {
		cnt[ch-'a']++
	}
	for _, ch := range ransomNote {
		idx := ch - 'a'
		cnt[idx]--
		if cnt[idx] < 0 {
			return false // Дефицит символа.
		}
	}
	return true
}
```

> “I treat magazine characters as a frequency budget and fail immediately on deficit while consuming ransom note symbols.”

- [Ransom Note на LeetCode](https://leetcode.com/problems/ransom-note/)
- [Оглавление книги](./README.md)
