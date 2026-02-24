# 44. Serialize and Deserialize Binary Tree: контракт формата данных

Это уже почти системный дизайн в миниатюре. Задача не про «обойти дерево», а про стабильный контракт между записью и чтением.

Нужен чёткий протокол:
- выбираем обход (обычно BFS или preorder);
- явно кодируем `null`-узлы;
- фиксируем разделитель и правила парсинга;
- проверяем, что `deserialize(serialize(tree))` восстанавливает структуру без искажений.

Почему это важно:
- если пропустить `null`, форма дерева теряется;
- если формат нестрогий, появятся несовместимые версии;
- если нет явного контракта, отладка становится дорогой.

Сложность:
- время: **O(n)** для serialise и deserialise;
- память: **O(n)**.

Термины:
- **format contract** — контракт формата;
- **round-trip integrity** — целостность двойного преобразования;
- **null sentinel** — маркер пустого узла.

Пример на JavaScript (preorder):

```javascript
function serialize(root) {
  const out = [];

  function dfs(node) {
    if (!node) {
      out.push('#');
      return;
    }
    out.push(String(node.val));
    dfs(node.left);
    dfs(node.right);
  }

  dfs(root);
  return out.join(',');
}

function deserialize(data) {
  const tokens = data.split(',');
  let idx = 0;

  function build() {
    if (tokens[idx] === '#') {
      idx++;
      return null;
    }

    const node = { val: Number(tokens[idx]), left: null, right: null };
    idx++;
    node.left = build();
    node.right = build();
    return node;
  }

  return build();
}
```

Пример ответа на интервью:

> “I define a deterministic preorder format with null sentinels, then parse it with the same grammar. The key requirement is round-trip integrity, not a specific traversal.”  
> [«Я задаю детерминированный preorder-формат с null-маркерами, затем парсю его той же грамматикой. Ключевое требование — целостность round-trip, а не конкретный тип обхода».]

Пара фраз для памяти:
- “No contract, no compatibility.”  
  [«Нет контракта — нет совместимости».]
- “Round-trip is the truth test.”  
  [«Round-trip — проверка истины».]

Где это в работе: обмен структурой данных между сервисами, кэширование деревьев решений, хранение и восстановление состояния пользовательских сценариев.

Сильный момент: вы уже думаете как инженер интерфейсов данных, а не только как решатель алгоритмических пазлов.

Полезные ссылки:
- [Serialize and Deserialize Binary Tree на LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [Глава про K Closest Points to Origin](./43_k_closest_points_heap_vs_quickselect_ru.md)
- [Оглавление книги](./README.md)
