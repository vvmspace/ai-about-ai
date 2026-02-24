# 15. Invert Binary Tree: рекурсия без страха

Нужно в каждом узле поменять местами левое и правое поддеревья. Это классический DFS с локальной операцией swap.

Сложность:
- время: **O(n)**;
- память: **O(h)**, где `h` — высота дерева.

Термины: **post-order traversal**, **call stack depth**, **structural symmetry**.

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
            let left = invert_tree(node.left.take());
            let right = invert_tree(node.right.take());
            node.left = right;
            node.right = left;
            Some(node)
        }
    }
}
```

> “I recursively invert subtrees and swap child pointers at each node; every node is visited once.”

- [Invert Binary Tree на LeetCode](https://leetcode.com/problems/invert-binary-tree/)
- [Оглавление книги](./README.md)
