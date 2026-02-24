# 45. Least Recently Used Cache: hash map + двусвязный список

Это одна из самых показательных задач интервью: требуется не только идея, но и строгий контракт операций за O(1).

Требования обычно такие:
- `get(key)` — вернуть значение и обновить «свежесть»;
- `put(key, value)` — вставить или обновить;
- при переполнении удалить самый «старый» элемент.

Надёжная архитектура:
- hash map: `key -> node` для O(1) доступа;
- doubly linked list для O(1) удаления/вставки;
- голова списка — самый свежий, хвост — кандидат на вытеснение.

Сложность:
- `get`: **O(1)**;
- `put`: **O(1)**;
- память: **O(capacity)**.

Термины:
- **eviction policy** — политика вытеснения;
- **recency order** — порядок недавности;
- **constant-time mutation** — мутация за константное время.

Пример на Python:

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = Node()  # sentinel
        self.tail = Node()  # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _insert_front(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._insert_front(node)
            return

        node = Node(key, value)
        self.map[key] = node
        self._insert_front(node)

        if len(self.map) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]
```

Пример ответа на интервью:

> “I combine hashmap for direct lookup with a doubly linked list for recency ordering. Every get/put move is O(1), and eviction is just removing the tail predecessor.”  
> [«Я совмещаю hashmap для прямого доступа и двусвязный список для порядка недавности. Любое перемещение в get/put — O(1), а вытеснение — это удаление предшественника хвоста».]

Пара фраз для памяти:
- “Fast lookup. Fast reorder.”  
  [«Быстрый доступ. Быстрый reorder».]
- “Policy lives in structure.”  
  [«Политика живёт в структуре».]

Где это в работе: API-кэш, кэш конфигураций, локальные hot-данные в высоконагруженных сервисах.

И это важная веха: вы уже умеете объяснить связку структуры данных и продуктового поведения. На собеседовании это звучит очень убедительно.

Полезные ссылки:
- [LRU Cache на LeetCode](https://leetcode.com/problems/lru-cache/)
- [Глава про Serialize and Deserialize Binary Tree](./44_serialize_deserialize_binary_tree_format_contract_ru.md)
- [Оглавление книги](./README.md)
