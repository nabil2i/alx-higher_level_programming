#!/usr/bin/python3


class Node:
    """Node of a singly linked list

        Attributes:
            __data (int): data of the node
            __next_node (Node): next node
    """

    def __init__(self, data, next_node=None):
        """Initializes a node

        Args:
            data (int): data of a node
            next_node (Node): next node

        Returns:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of __data

        Returns:
            The data of a node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter of __data

        Args:
            value (int): value of the data

        Returns:
            None
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """getter of __next_node

        Returns:
            Next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of __next_node

        Args:
            value (Node): the next node

        Returns:
            None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list

    Attributes:
        __head (Node): head of the list
    """

    def __init__(self):
        """Initializes a singly linked list"""
        self.head = None

    def __str__(self):
        """To print in the file"""
        my_str = ""
        node = self.head
        while node:
            my_str += str(node.data)
            my_str += '\n'
            node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        """Inserts a new node

        Args:
            value (int): data to insert

        Returns:
            None
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = nodie.next_node
        node.next_node = new_node
