"""Allows you to search a sorted list in O(log n) vs. typical O(n) runtime.
Examine middle item, and if target value smaller, move halfway to left. Vice
versa."""


class BinarySearchNode(object):
    """Binary tree node."""

    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.data

    def find(self, sought):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        # establish as self so you can refer to current node in algorithm
        current = self

        # loop in place until sought value found
        while current:

            print "checking ", current.data

            # if data matches parameter inputted in this method, return node
            if current.data == sought:
                return current

            # traverse left or right down the BST
            elif sought < current.data:
                current = current.left

            elif sought > current.data:
                current = current.right


if __name__ == '__main__':
    # Create sample tree and search for nodes in it

    # Instantiate nodes; observe how parameters are written (current, L, R)
    apple = BinarySearchNode("apple")
    ghost = BinarySearchNode("ghost")
    fence = BinarySearchNode("fence", apple, ghost)
    just = BinarySearchNode("just")
    jackal = BinarySearchNode("jackal", fence, just)
    zebra = BinarySearchNode("zebra")
    pencil = BinarySearchNode("pencil", None, zebra)
    mystic = BinarySearchNode("mystic")
    nerd = BinarySearchNode("nerd", mystic, pencil)
    money = BinarySearchNode("money", jackal, nerd)

    # How to use: var_name_of_node.find(sought_value)
    print "nerd = ", money.find("nerd")      # should find
    print "banana = ", money.find("banana")  # shouldn't find
