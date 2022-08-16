from typing import Optional


class Node:
    """
    Provide necessary documentation
    """
    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """
    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        # Write code here
        current=self.head
        while(current):
            current=current.next
        current=Node(data)

    def status(self):
        """
        It prints all the elements of list.
        """
        current=self.head
        while(current):
            println(current.data)
            current=current.next


class Solution:
    """
    Provide necessary documentation
    """
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        # Write code here
        current =first_list.head
        F_digits=0
        while(current):
            F_digits=F_digits+1
            current=current.next
        
        S_digits=0
        current =second_list.head
        while(current):
            S_digits=S_digits+1
            current=current.next
            
        ans=LinkedList()
        F_current=first_list.head
        S_current=second_list.head
        if F_digits>S_digits:
            for i in range(S_digits):
                ans.insert_at_end(F_current.data+S_current.data)
                F_current=F_current.next
                S_current=S_current.next
        else:
            for i in range(F_digits):
                ans.insert_at_end(F_current.data+S_current.data)
                F_current=F_current.next
                S_current=S_current.next
            
            
            
        
        
        

# Do not edit the following code      
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
