# Esercizio 1

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal 
# stack (push, top, pop, and empty).

# Implement the MyStack class:

# - push(x: int) -> None: Pushes element x to the top of the stack.
# - pop() -> None Removes the element on the top of the stack and returns it.
# - pop() -> None Returns the element on the top of the stack.
# - empty() -> None Returns true if the stack is empty, false otherwise.


class Queue:
    def __init__(self) -> None:
        self.queue: list = []
    

        

class MyStack:
    def __init__(self) -> None:
        self.queue = Queue()
        
    def push(self, element: int)-> None:
        self.queue.queue.insert(0, element)
       
    def pop(self) -> int:
        element = self.queue.queue.pop(0)
        return element
    
    def top(self)-> int:
        return self.queue.queue[0]
    
    def empty(self)-> bool:
        if len(self.queue.queue) == 0:
            return True
        else:
            return False

# mystack = MyStack()
# mystack.push(1)
# mystack.push(2)
# print(mystack.top())    # Output: 2
# print(mystack.pop())    # Output: 2
# print(mystack.empty())  # Output: False
# print(mystack.pop())    # Output: 1
# print(mystack.empty())  # Output: True

# Esercizio 2
        

# Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a 
# linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is 
# not passed as a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.
 
# Model the Node and Linked List concepts using classes.



class Node:
    def __init__(self, value) -> None:  # standard
        self.value = value
        self.next = None               

class LinkedList:
    def __init__(self):     # standard
        self.head = None     

    def append(self, value)-> None:
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.value = Node(value)
    
    def get_node(self, number: int):
        current = self.head
        counter = 0
        while current.next is not None and counter < number:
            current = current.next
            counter += 1
        return current

def has_cycle(head: Node) -> list[int]:
    lista_controllo: list = []
    current = head
    while current.next is not None:
        lista_controllo.append(current)
        current = current.next
        if current in lista_controllo:
            return True
    return False
    

 	

# ll1 = LinkedList()
# for i in range(5):
#     ll1.append(i)
# node1 = ll1.get_node(1)  # Node with value 1
# node4 = ll1.get_node(4)  # Node with value 4
# node4.next = node1  # Creating a cycle
# print(has_cycle(ll1.head))

# Esercizio 3

# Given a string s which consists of lowercase or uppercase letters, write a function that returns the length 
# of the longest palindrome that can be built with those letters. Letters are case sensitive, for example, 
# "Aa" is not considered a palindrome here.

def longest_palindrome(s: str) -> int:
    dizionario_controllo = {}
    num = 0
    for x in s:
        if x not in dizionario_controllo:
            dizionario_controllo[x] = 1
        else:
            dizionario_controllo[x] += 1
    for x in dizionario_controllo.values():
        if x > 1:
            if x % 2 == 1:
                num += x - 1
            else:
                num += x
    if num % 2 == 0 and num < len(s):
        num += 1
        return num
    return num



 
# print(longest_palindrome("abccccdd"))
# print(longest_palindrome("abcabcabc"))
        

# Esercizio 4 

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2 into 
# a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
        
def merge(nums1: list, m, nums2: list, n):
    counter = 1
    control_number = len(nums1) - m
    while counter <= control_number:
        nums1.pop()
        counter += 1
    for x in nums2:
        nums1.append(x)
    nums1 = nums1.sort()
    return nums1




# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# merge(nums1, m, nums2, n)
# print(nums1)  
# [1, 2, 2, 3, 5, 6]

# Esercizio 5

# Given the head of a singly linked list, return true if it is a palindrome. Model the Node and Linked List concepts using classes.

              

class LinkedList:
    def __init__(self, head = None):     # standard
        self.head = head     

    def append(self, value)-> None:
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

class Node:
    def __init__(self, value) -> None:  # standard
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value) 
    
        
def is_palindrome(head: Node) -> list[int]:
    
    lista_controllo = []
    while head:
        lista_controllo.append(head.value)
        head = head.next
    return lista_controllo == lista_controllo[::-1]

   

# Esercizio 6

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if 
# the input string is valid.

# An input string is valid if: 

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

def is_valid_parenthesis(s: str) -> bool:
    dict1: dict = {'(': 1, '[': 2, '{': 3}
    dict2: dict = {')': 1, ']': 2, '}': 3}
    lista_controllo = []
    for x in s:
        if x in list(dict1.keys()):
            lista_controllo.append(dict1[x])
        else:
            if lista_controllo[-1]-dict2[x] == 0:
                lista_controllo.pop(-1)
            else:
                return False
    return True


# print(is_valid_parenthesis("()"))
# print(is_valid_parenthesis("()[]{}"))
# print(is_valid_parenthesis("(]"))
# print(is_valid_parenthesis("([)]"))      # Output: False
# print(is_valid_parenthesis("{[]}"))
# print(is_valid_parenthesis(""))