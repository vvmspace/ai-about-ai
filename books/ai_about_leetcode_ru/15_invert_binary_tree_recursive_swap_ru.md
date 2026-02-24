# 15. Invert Binary Tree: рекурсия без страха

Эта задача часто кажется слишком простой, и именно поэтому на ней видно качество мышления. Нужно не «угадать», а спокойно зафиксировать инвариант: в каждом узле мы меняем местами левое и правое поддеревья.

Сложность:
- время: **O(n)** — каждый узел посещается ровно один раз;
- память: **O(h)** — глубина рекурсии, где `h` высота дерева.

Неочевидные термины: **structural symmetry**, **recursive descent**, **stack depth bound**.

```rust
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Box<TreeNode>>,
    pub right: Option<Box<TreeNode>>,
}

pub fn invert_tree(root: Option<Box<TreeNode>>) -> Option<Box<TreeNode>> {
    match root {
        None => None,
        Some(mut node) => {
            // Рекурсивно инвертируем поддеревья.
            let left = invert_tree(node.left.take());
            let right = invert_tree(node.right.take());

            // Меняем их местами.
            node.left = right;
            node.right = left;

            Some(node)
        }
    }
}
```

> “I recursively invert both subtrees and swap child pointers at each node; each node is processed exactly once.”

- [Invert Binary Tree на LeetCode](https://leetcode.com/problems/invert-binary-tree/)
- [Оглавление книги](./README.md)
