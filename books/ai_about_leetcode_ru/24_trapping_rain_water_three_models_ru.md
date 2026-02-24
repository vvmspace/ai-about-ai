# 24. Trapping Rain Water: одна задача, три инженерные модели

Задача известная, но ценность в том, что она учит выбирать модель под ограничения, а не влюбляться в один шаблон.

Есть три рабочих подхода:
- префикс/постфикс максимумы;
- два указателя;
- монотонный стек.

Для интервью чаще всего достаточно двух указателей: меньше памяти и хороший баланс ясности.

Сложность (два указателя):
- время: **O(n)**;
- память: **O(1)**.

Неочевидные термины:
- **water level bound** — уровень воды в позиции, ограниченный левым и правым максимумом;
- **running maxima** — текущие максимумы слева и справа;
- **state compression** — сокращение памяти за счёт хранения только нужного состояния.

Пример на JavaScript (два указателя):

```javascript
function trap(height) {
  let left = 0;
  let right = height.length - 1;
  let leftMax = 0;
  let rightMax = 0;
  let water = 0;

  while (left < right) {
    if (height[left] < height[right]) {
      leftMax = Math.max(leftMax, height[left]);
      water += leftMax - height[left];
      left++;
    } else {
      rightMax = Math.max(rightMax, height[right]);
      water += rightMax - height[right];
      right--;
    }
  }

  return water;
}
```

Интервью-ответ:

> “I compute trapped water with two pointers and running maxima. At each step, the lower side defines a safe bound, so I can accumulate water immediately and move inward in linear time.”  
> [«Я считаю объём воды двумя указателями и текущими максимумами. На каждом шаге более низкая сторона задаёт безопасную границу, поэтому можно сразу добавлять вклад и двигаться внутрь за линейное время».]

Пара фраз:
- “Boundaries define volume.”  
  [«Границы определяют объём».]
- “Choose the model, then execute.”  
  [«Сначала выбери модель, затем исполняй».]

Где это в работе: оценка буферной ёмкости между пиковыми нагрузками, расчёт накопления задержек, моделирование провалов в телеметрии.

Полезные ссылки:
- [Trapping Rain Water на LeetCode](https://leetcode.com/problems/trapping-rain-water/)
- [Глава про Container With Most Water](./22_container_with_most_water_two_pointers_ru.md)
- [Оглавление книги](./README.md)
