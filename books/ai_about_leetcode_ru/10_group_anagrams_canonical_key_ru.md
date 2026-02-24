# 10. Group Anagrams: каноническая форма ключа

В этой задаче важно быстро увидеть модель: мы не сравниваем каждую строку с каждой, а приводим слова к общей канонической форме и группируем по ключу.

Подхода два: сортировать символы или строить частотный ключ. Для универсальности чаще используют сортировку символов.

Сложность:
- время: **O(n * k log k)**, где `n` — число слов, `k` — длина слова;
- память: **O(n * k)** на хранение групп.

Неочевидные термины: **canonical representation**, **hash bucketing**, **collision domain**.

```python
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = "".join(sorted(s))  # Канонический ключ.
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
```

> “I map each word to a canonical key and bucket by that key. This avoids pairwise comparisons and scales linearly in the number of words, with key-construction cost per word.”

- [Group Anagrams на LeetCode](https://leetcode.com/problems/group-anagrams/)
- [Оглавление книги](./README.md)
