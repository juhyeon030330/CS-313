class QueueCapacityTypeError(Exception):
    pass


class QueueCapacityBoundError(Exception):
    pass


class QueueIsFull(Exception):
    pass


class QueueIsEmpty(Exception):
    pass


class StackCapacityTypeError(Exception):
    pass


class StackIsFull(Exception):
    pass


class StackIsEmpty(Exception):
    pass


class StackCapacityBoundError(Exception):
    pass


class Node:

    def __init__(self, data=None):
        """

        """
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        self.data = data
        self.next = None


class Queue:

    def __init__(self, capacity):
        """

        """
        if type(capacity) != int:
            raise QueueCapacityTypeError('Invalid type of capacity')
        elif capacity < 1:
            raise QueueCapacityBoundError('Invalid capacity')
        else:
            ####### YOUR CODE STARTS HERE #######
            # raise NotImplementedError()
            self.head = None
            self.tail = None
            self.capacity = capacity
            self.currentSize = 0


    def enqueue(self, item):
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        if self.isFull():
            raise QueueIsFull('queue full.')
        else:
            if self.isEmpty():
                new_node = Node(item)
                self.head = new_node
                self.tail = new_node
            else:
                new_node = Node(item)
                self.tail.next = new_node
                self.tail = new_node
                
            self.currentSize = self.currentSize + 1
            return True

    def dequeue(self):
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        if self.isEmpty():
            raise QueueIsEmpty('queue empty.')
        else:
            remove = self.head
            self.head = self.head.next
            self.currentSize -= 1

            if self.head is None:
                self.tail = None

            remove.next = None
            return remove.data


    def front(self):
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        if self.isEmpty():
            return False
        else:
            return self.head.data

    def isEmpty(self):
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        if self.currentSize == 0:
            return True
        else:
            return False 

    def isFull(self):
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        if self.currentSize == self.capacity:
            return True
        else:
            return False


class Stack:

    def __init__(self, capacity):
        """

        """
        if type(capacity) != int:
            raise StackCapacityTypeError('Invalid type of capacity')
        elif capacity < 1:
            raise StackCapacityBoundError('Invalid capacity')
        else:
            ####### YOUR CODE STARTS HERE #######
            # raise NotImplementedError()
            self.head = None
            self.capacity = capacity
            self.currentSize = 0

    def push(self, item):
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        if self.isFull():
            raise StackIsFull("stack full.")
        else:
            new = Node(item)
            new.next = self.head
            self.head = new
            
            self.currentSize += 1
            return True


    def pop(self):
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        if self.isEmpty():
            raise StackIsEmpty("stack empty")
        rm = self.head
        self.head = self.head.next
        rm.next = None

        self.currentSize -= 1
        return rm.data



    def peek(self):
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        if self.isEmpty():
            return False
        else:
            return self.head.data

    def isEmpty(self):
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        if self.currentSize == 0:
            return True
        else:
            return False

    def isFull(self):
        ####### YOUR CODE STARTS HERE #######
        # raise NotImplementedError()
        if self.currentSize == self.capacity:
            return True
        else:
            return False