# BINARY SEARCH TREE (BST)


class Node:
    def __init__(self, key, value, left, right):
        self.key = key  # Key
        self.value = value  # Value
        self.left = left  # Left child (Node)
        self.right = right  # Right child (Node)


class BinarySearchTree:
    def __init__(self):
        self.root = None  # Root node (Node)

    def search(self, key):
        """Search node w.r.t. key"""
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key, value):
        """Add node to the BST"""

        def add_node(node, key, value):
            """node를 루트로 하는 서브 트리에 키가 key이고, 값이 value인 노드를 삽입"""
            if key == node.key:
                return False  # key가 이진검색트리에 이미 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key):
        """Delete node w.r.t. key"""
        p = self.root  # Current node
        parent = None  # Parent node
        is_left_child = True  # Check whether "p" is the left-child of "parent"

        # Search node w.r.t. "key"
        while True:
            if p is None:  # Search failure
                return False  # The node with "key" does not exist 

            if key == p.key:  # Search success
                break
            else:
                parent = p  # Set "parent" as "p"
                if key < p.key:  # Move to the left-child
                    is_left_child = True
                    p = p.left
                else:  # Move to the right-child
                    is_left_child = False
                    p = p.right

        # (A) "p" does not have left-child & right-child
        # (B) If "p" does not have left-child
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None:  # (B) If "p" does not have right-child
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:  # (C) "p" has both left-child & right-child
            # todo: Write code here!
            pass

        return True

    def print_in_order(self) -> None:
        """Print all node in the order"""

        def print_subtree(node: Node):
            """Print all node in the order(sub-tree)"""
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key}  {node.value}')
                print_subtree(node.right)

        print_subtree(self.root)

    def min_key(self):
        """Return the minimum key"""
        # todo: Write code here!
        return 0

    def max_key(self):
        """Return the maximum key"""
        # todo: Write code here!
        return 0
