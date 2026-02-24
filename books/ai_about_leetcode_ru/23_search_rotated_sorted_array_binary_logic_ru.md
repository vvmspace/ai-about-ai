# 23. Search in Rotated Sorted Array: бинарный поиск в сломанном порядке

Именно здесь видно, умеете ли вы сохранять холодную голову. Массив «почти отсортирован», но одно смещение ломает привычный шаблон.

Ключевой факт: в каждом шаге хотя бы одна половина всё ещё отсортирована.
- если левая половина отсортирована, проверяем, лежит ли `target` внутри неё;
- иначе правая половина отсортирована, проверяем её диапазон.

Сложность:
- время: **O(log n)**;
- память: **O(1)**.

Неочевидные термины:
- **rotated monotonic segments** — монотонные сегменты после циклического сдвига;
- **range membership test** — проверка принадлежности цели отсортированному диапазону;
- **decision partition** — разбиение пространства поиска по логическим условиям.

Пример на Go:

```go
package main

func search(nums []int, target int) int {
	left, right := 0, len(nums)-1

	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] == target {
			return mid
		}

		if nums[left] <= nums[mid] { // Левая половина отсортирована.
			if nums[left] <= target && target < nums[mid] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else { // Правая половина отсортирована.
			if nums[mid] < target && target <= nums[right] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}

	return -1
}
```

Интервью-ответ:

> “I keep binary search and add one extra invariant: at least one half is sorted after rotation. Each iteration identifies the sorted half, tests target membership, and discards the other half.”  
> [«Я сохраняю бинарный поиск и добавляю один инвариант: после ротации хотя бы одна половина отсортирована. На каждой итерации определяю отсортированную половину, проверяю вхождение target и отбрасываю другую».]

Пара фраз:
- “Rotation changes shape, not discipline.”  
  [«Ротация меняет форму, но не дисциплину».]
- “One sorted half is enough.”  
  [«Одной отсортированной половины достаточно».]

Где это в работе: поиск события в циклических логах, навигация по кольцевым буферам, восстановление позиции в сдвинутых индексах.

Полезные ссылки:
- [Search in Rotated Sorted Array на LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [Глава про Binary Search](./08_binary_search_boundary_discipline_ru.md)
- [Оглавление книги](./README.md)
