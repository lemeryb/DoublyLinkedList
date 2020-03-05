# Title: Doubly Linked List
# Author: Benjamin Lemery
# Date: 3/4/20
# This program demonstrates how to create and manipulate doubly linked lists


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def add_to_start(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_to_end(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        node = self.head
        while node == Node(data):
            node.next = new_node
            new_node.prev = node