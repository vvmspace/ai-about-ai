# 02. Merge Two Sorted Lists: линейное слияние как базовый рефлекс

Эта задача часто маскируется под «лёгкую». Но интервьюер тут проверяет не сложность алгоритма, а инженерную чистоту: не теряете ли вы узлы, не путаете ли ссылки, умеете ли держать инвариант.

Есть два отсортированных связных списка. Нужно слить их в один отсортированный. Ключевая идея — всегда брать меньшую голову и двигать соответствующий указатель.

Почему это работает? Инвариант такой: *на каждом шаге результирующий хвост уже отсортирован и содержит минимально возможные элементы из ещё не обработанных*.

Сложность:
- время: **O(n + m)**, каждый узел посещается один раз;
- память: **O(1)** для итеративной версии (не считая входных данных).

Неочевидные термины, которые полезно проговорить:
- **sentinel node** (*dummy head*) — фиктивный стартовый узел, упрощающий обработку первого элемента;
- **pointer hygiene** — дисциплина обновления ссылок без «утечки» узлов;
- **stability of merge** — при равных значениях сохраняется относительный порядок элементов внутри каждого источника.

Пример на Rust (итеративно):

```rust
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

pub fn merge_two_lists(
    mut l1: Option<Box<ListNode>>,
    mut l2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    let mut dummy = Box::new(ListNode::new(0)); // Sentinel node.
    let mut tail = &mut dummy;

    while l1.is_some() && l2.is_some() {
        // Сравниваем головы и вынимаем минимальный узел.
        let take_l1 = l1.as_ref().unwrap().val <= l2.as_ref().unwrap().val;

        if take_l1 {
            let mut node = l1.take().unwrap();
            l1 = node.next.take(); // Переносим владение следующей ссылкой.
            tail.next = Some(node); // Пришиваем узел к хвосту результата.
        } else {
            let mut node = l2.take().unwrap();
            l2 = node.next.take();
            tail.next = Some(node);
        }

        tail = tail.next.as_mut().unwrap(); // Сдвигаем хвост.
    }

    // Дописываем остаток непустого списка.
    tail.next = if l1.is_some() { l1 } else { l2 };

    dummy.next
}
```

Интервью-ответ:

> “I merge in one pass using a sentinel head and a moving tail pointer. At each step I append the smaller current node, preserving sorted order. This yields O(n+m) time and constant auxiliary space.”  
> [«Я выполняю слияние за один проход через фиктивную голову и подвижный хвост. На каждом шаге добавляю меньший текущий узел, сохраняя сортировку. Это даёт O(n+m) по времени и константную дополнительную память».]

Пара фраз:
- “The invariant lives in the tail.”  
  [«Инвариант живёт в хвосте результата».]
- “Sentinel nodes remove edge-case noise.”  
  [«Фиктивные узлы убирают шум крайних случаев».]

Где это нужно в работе: merge потоков событий по времени, слияние paginated данных из двух источников, объединение отсортированных батчей при ETL.

Полезные ссылки:
- [Merge Two Sorted Lists на LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)
- [Оглавление книги](./README.md)
