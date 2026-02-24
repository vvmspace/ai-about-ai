# 10. Group Anagrams: канонический ключ для группировки

Когда люди впервые видят эту задачу, они часто начинают сравнивать каждую строку с каждой. Это прямой путь к O(n²). Нормальный инженерный путь — сначала нормализовать представление, потом группировать.

Идея: каждая анаграмма должна иметь один и тот же ключ.
- вариант 1: отсортировать символы строки;
- вариант 2: использовать вектор частот как ключ.

Для общего случая берём сортировку символов.

Сложность:
- время: **O(n * k log k)**, где `n` — число слов, `k` — средняя длина слова;
- память: **O(n * k)** для хранения групп и ключей.

Термины: **canonical form**, **bucketization**, **key stability**.

```python
def group_anagrams(strs):
    groups = {}

    for s in strs:
        key = ''.join(sorted(s))  # Канонический ключ: одинаков для всех анаграмм.
        if key not in groups:
            groups[key] = []
        groups[key].append(s)     # Добавляем слово в нужную корзину.

    return list(groups.values())
```

> “I map each word to a canonical representation and group by that key, avoiding pairwise string comparison.”

- [Group Anagrams на LeetCode](https://leetcode.com/problems/group-anagrams/)
- [Оглавление книги](./README.md)
