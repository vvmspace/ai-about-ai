# 41. Find Minimum in Rotated Sorted Array: ещё один поворот бинарного поиска

На первый взгляд это «почти обычный binary search». На практике ошибка в одном сравнении ломает всё решение.

Опорная мысль:
- массив отсортирован, но разрезан в точке pivot;
- правая часть всегда содержит «хвост» с минимальным элементом;
- сравнение `nums[mid]` с `nums[right]` говорит, в какой половине лежит минимум.

Правило перехода:
- если `nums[mid] > nums[right]`, минимум строго правее `mid`, делаем `left = mid + 1`;
- иначе минимум в левой половине, включая `mid`, делаем `right = mid`.

Сложность:
- время: **O(log n)**;
- память: **O(1)**.

Термины:
- **rotation pivot** — точка поворота;
- **monotonic half** — монотонная половина;
- **search invariant** — инвариант области поиска.

Пример на Rust:

```rust
pub fn find_min(nums: Vec<i32>) -> i32 {
    let mut left = 0usize;
    let mut right = nums.len() - 1;

    while left < right {
        let mid = left + (right - left) / 2;
        if nums[mid] > nums[right] {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    nums[left]
}
```

Пример ответа на интервью:

> “I keep a binary-search invariant over the answer range: compare mid with right, discard the sorted half that cannot contain the minimum, and converge to one index.”  
> [«Я держу инвариант бинарного поиска по диапазону ответа: сравниваю середину с правой границей, отбрасываю отсортированную половину, которая не может содержать минимум, и схожусь к одному индексу».]

Пара фраз для памяти:
- “Compare with right, not with hope.”  
  [«Сравнивай с right, а не с надеждой».]
- “Invariant first. Index later.”  
  [«Сначала инвариант. Потом индекс».]

Где это в работе: поиск минимальной версии после циклических релизов, анализ тайм-серий после сдвига окна, диагностика «точки разрыва» в упорядоченных логах.

Отличный этап прогресса: вы не просто применили бинарный поиск, а сформулировали его как контракт. На интервью это звучит очень взрослым языком.

Полезные ссылки:
- [Find Minimum in Rotated Sorted Array на LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [Глава про Maximum Product Subarray](./40_maximum_product_subarray_max_min_tracking_ru.md)
- [Оглавление книги](./README.md)
