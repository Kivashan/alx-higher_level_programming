#!/usr/bin/python3
'''A module defining a singly_linked list class'''


class Node:
    '''A class defining a Node object, part of a singly_linked list'''

    def __init__(self, data, next_node=None):
        '''Method initializing a Node object

        Args:
            Param1 (self): First parameter
            Param2 (int): Second Parameter
            Param3 (Node): Third Parameter, of type Node
        '''

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Getter method for data attribute'''
        return self.__data

    @data.setter
    def data(self, value):
        '''Setter method for data attribute'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        '''Getter method for next_node attribute'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Setter method for next_node attribute'''
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    '''A class defining a class called SinglyLinkedList'''

    def __init__(self):
        '''Method initializing a SinglyLinkedList object

        Args:
            Param1 (self): First Parameter
        '''

        self.__head = list()

    def __str__(self):
        '''String representation for SinglyLinkedList object'''
        if len(self.__head) == 0:
            return ""
        else:
            string = ""
            for i in self.__head:
                string = string + str(i.data)
                if i != len(self.__head) - 1:
                    string = string + "\n"
            return string

    def sorted_insert(self, value):
        '''Method that inserts a value into a SinglyLinkedList object'''
        # if list is empty
        if len(self.__head) == 0:
            new_node = Node(value)          # create new node
            self.__head.append(new_node)    # add new node to linked list
        else:
            # if list is not empty, iterate through list using for loop
            for index in range(len(self.__head)):
                if value < self.__head[index].data:  # checks if value is less that the data at head[index]
                    new_node = Node(value, self.__head[index])   # create a new node
                    self.__head[index - 1].next_node = new_node  # link element at previous index to new_node
                    self.__head.insert(index, new_node)         # link new_node to current element
                    break
                # checks if this is the last element in the list, if so create new node and append to list, also link
                # last element in list to the new_node
                elif index == len(self.__head) - 1:
                    new_node = Node(value, None)
                    self.__head[index].next_node = new_node
                    self.__head.append(new_node)
