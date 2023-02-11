class Tree:

    def __init__(self, value_node):
        self.value_node = value_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value_node)

    def add_nodes_from_lst(self, lst):
        for value_node in lst:
            self.insert(value_node)


    def insert(self, value_node):
        if self.value_node:
            if value_node < self.value_node:
                if self.left is None:
                    self.left = Tree(value_node)
                else:
                    self.left.insert(value_node)
            elif value_node > self.value_node:
                if self.right is None:
                    self.right = Tree(value_node)
                else:
                    self.right.insert(value_node)
        else:
            self.value_node = value_node


    def findval(self, find_val):
        if find_val < self.value_node:
            if self.left is None:
                return f"{find_val} NOT FOUND"
            return self.left.findval(find_val)
        elif find_val > self.value_node:
            if self.right is None:
                return f"{find_val} NOT FOUND"
            return self.right.findval(find_val)
        else:
            print(f"{self.value_node} IS FOUND")


    def check_node(self, find_val):
        if not find_val:
            return None
        if find_val < self.value_node:
            if self.left is None:
                return False
            return bool(self.left.check_node(find_val))
        elif find_val > self.value_node:
            if self.right is None:
                return False
            return bool(self.right.check_node(find_val))
        else:
            return bool(self)


    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value_node),
        if self.right:
            self.right.print_tree()


    def min_value_node(self):
         if self.left is None:
             return self.value_node
         return self.left.min_value_node()

    def max_value_node(self):
         if self.right is None:
             return self.value_node
         return self.right.max_value_node()


    def delete_node(self, value):
        if self is None:
            return self
        if value < self.value_node:
            self.left = self.left.delete_node(value)
            return self
        if value > self.value_node:
            self.right = self.right.delete_node(value)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        char = self.right
        while self.min_value_node().left:
            char = char.left
        self.value_node = char.value_node
        self.right = self.right.delete_node(char.value_node)
        return self


tree = Tree(10)
tree.add_nodes_from_lst([10, 4, 18, 2, 31])

tree.insert(29)
tree.print_tree()
print(f"min value node = {tree.min_value_node()}")
print(f"max value node = {tree.max_value_node()}")

