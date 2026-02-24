# 22. Container With Most Water: два указателя и строгая логика шага

Эта задача кажется геометрической. На практике она про доказуемый выбор, а не про интуицию.

Берём две границы: левую и правую. Площадь определяется как:
`min(height[left], height[right]) * (right - left)`.

Почему двигаем меньшую стенку:
- высота ограничена меньшей из двух;
- если сдвинуть большую, ограничение не улучшится, а ширина уменьшится;
- значит шанс улучшить площадь есть только при сдвиге меньшей.

Сложность:
- время: **O(n)**;
- память: **O(1)**.

Неочевидные термины:
- **dominant constraint** — ограничивающий фактор, определяющий максимум;
- **pointer elimination** — исключение заведомо бесполезных состояний;
- **monotone shrink** — монотонное сужение окна поиска.

Пример на Python:

```python
def max_area(height):
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        h = min(height[left], height[right])
        width = right - left
        best = max(best, h * width)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return best
```

Интервью-ответ:

> “I use two pointers and move only the shorter side. The shorter wall is the active constraint; moving the taller one cannot improve capacity while width strictly decreases.”  
> [«Я использую два указателя и двигаю только более низкую сторону. Низкая стенка — активное ограничение; сдвиг более высокой не может улучшить объём, пока ширина строго уменьшается».]

Пара фраз:
- “Move the bottleneck, not the decoration.”  
  [«Двигай узкое место, а не декорацию».]
- “Proof beats guesswork.”  
  [«Доказательство сильнее догадки».]

Где это в работе: подбор пар параметров с максимальной пропускной способностью, оценка ёмкости канала между двумя ограничениями, оптимизация окон агрегации.

Полезные ссылки:
- [Container With Most Water на LeetCode](https://leetcode.com/problems/container-with-most-water/)
- [Глава про 3Sum](./20_3sum_two_pointers_dedup_ru.md)
- [Оглавление книги](./README.md)
