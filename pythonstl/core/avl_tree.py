"""
AVL Tree implementation for PythonSTL.

This module provides a pure-Python self-balancing Binary Search Tree (AVL Tree)
to ensure sorted order and O(log n) operation complexity for Python fallbacks of
associative containers (set and map), matching C++ STL and Rust BTree semantics.
"""

from typing import TypeVar, Generic, Optional, Generator, Tuple, Any

K = TypeVar('K')
V = TypeVar('V')


class AVLNode(Generic[K, V]):
    """A node in the AVL Tree."""
    __slots__ = ('key', 'value', 'left', 'right', 'height')

    def __init__(self, key: K, value: Optional[V] = None) -> None:
        self.key = key
        self.value = value
        self.left: Optional[AVLNode[K, V]] = None
        self.right: Optional[AVLNode[K, V]] = None
        self.height: int = 1


class AVLTree(Generic[K, V]):
    """
    A self-balancing binary search tree (AVL Tree) implementing dict/set-like operations.
    """

    def __init__(self) -> None:
        self.root: Optional[AVLNode[K, V]] = None
        self._size: int = 0

    def __len__(self) -> int:
        """Return the number of nodes in the tree."""
        return self._size

    def __contains__(self, key: K) -> bool:
        """Check if a key exists in the tree."""
        return self._find(self.root, key) is not None

    def _find(self, node: Optional[AVLNode[K, V]], key: K) -> Optional[AVLNode[K, V]]:
        curr = node
        while curr:
            if key == curr.key:
                return curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def __getitem__(self, key: K) -> V:
        """Get the value associated with the key."""
        node = self._find(self.root, key)
        if node is None:
            raise KeyError(key)
        return node.value

    def _get_height(self, node: Optional[AVLNode[K, V]]) -> int:
        return node.height if node else 0

    def _get_balance(self, node: Optional[AVLNode[K, V]]) -> int:
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, y: AVLNode[K, V]) -> AVLNode[K, V]:
        x = y.left
        assert x is not None
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1

        return x

    def _left_rotate(self, x: AVLNode[K, V]) -> AVLNode[K, V]:
        y = x.right
        assert y is not None
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1

        return y

    def __setitem__(self, key: K, value: V) -> None:
        """Insert or update a key-value pair in the tree."""
        self.root = self._insert(self.root, key, value)

    def _insert(self, node: Optional[AVLNode[K, V]], key: K, value: V) -> AVLNode[K, V]:
        # 1. Standard BST insertion
        if not node:
            self._size += 1
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            # Key already exists, update value and return (no size change or rebalancing needed)
            node.value = value
            return node

        # 2. Update height of this ancestor node
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

        # 3. Get the balance factor
        balance = self._get_balance(node)

        # Left Left Case
        if balance > 1 and node.left and key < node.left.key:
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and node.right and key > node.right.key:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and node.left and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and node.right and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def add(self, key: K) -> None:
        """Add a key to the tree (value defaults to None)."""
        self[key] = None

    def pop(self, key: K, default: Any = KeyError) -> Any:
        """Remove key and return the associated value."""
        node = self._find(self.root, key)
        if node is None:
            if default is not KeyError:
                return default
            raise KeyError(key)
        val = node.value
        self.root = self._delete(self.root, key)
        return val

    def discard(self, key: K) -> None:
        """Remove key from the tree if it exists, otherwise do nothing."""
        if key in self:
            self.root = self._delete(self.root, key)

    def _min_value_node(self, node: AVLNode[K, V]) -> AVLNode[K, V]:
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node: Optional[AVLNode[K, V]], key: K) -> Optional[AVLNode[K, V]]:
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if not node.left:
                temp = node.right
                self._size -= 1
                return temp
            elif not node.right:
                temp = node.left
                self._size -= 1
                return temp

            # Node with two children: Get the inorder successor
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)

        if not node:
            return node

        # Update height
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

        # Get balance factor
        balance = self._get_balance(node)

        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def __iter__(self) -> Generator[K, None, None]:
        """In-order traversal yielding keys."""
        yield from self._inorder(self.root)

    def _inorder(self, node: Optional[AVLNode[K, V]]) -> Generator[K, None, None]:
        if node:
            yield from self._inorder(node.left)
            yield node.key
            yield from self._inorder(node.right)

    def items(self) -> Generator[Tuple[K, V], None, None]:
        """In-order traversal yielding (key, value) pairs."""
        yield from self._inorder_items(self.root)

    def _inorder_items(self, node: Optional[AVLNode[K, V]]) -> Generator[Tuple[K, V], None, None]:
        if node:
            yield from self._inorder_items(node.left)
            yield (node.key, node.value)
            yield from self._inorder_items(node.right)

    def keys(self) -> Generator[K, None, None]:
        """In-order traversal yielding keys."""
        yield from self

    def values(self) -> Generator[V, None, None]:
        """In-order traversal yielding values."""
        yield from self._inorder_values(self.root)

    def _inorder_values(self, node: Optional[AVLNode[K, V]]) -> Generator[V, None, None]:
        if node:
            yield from self._inorder_values(node.left)
            yield node.value
            yield from self._inorder_values(node.right)

    def copy(self) -> 'AVLTree[K, V]':
        """Create a copy of the AVL tree structure."""
        new_tree = AVLTree[K, V]()
        new_tree.root = self._copy_node(self.root)
        new_tree._size = self._size
        return new_tree

    def _copy_node(self, node: Optional[AVLNode[K, V]]) -> Optional[AVLNode[K, V]]:
        if not node:
            return None
        new_node = AVLNode(node.key, node.value)
        new_node.height = node.height
        new_node.left = self._copy_node(node.left)
        new_node.right = self._copy_node(node.right)
        return new_node

    def __eq__(self, other: object) -> bool:
        """Check equality with another AVL tree or dict (based on element order/keys)."""
        if isinstance(other, dict):
            return dict(self.items()) == other
        if not isinstance(other, AVLTree):
            return False
        if self._size != other._size:
            return False
        return list(self.items()) == list(other.items())

    def __repr__(self) -> str:
        return f"AVLTree({list(self.items())})"
