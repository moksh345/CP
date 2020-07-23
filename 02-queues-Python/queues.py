"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None,tail=None,queue=None):
        self.storage = [head]
        self.storage = [tail]
        queue=[]

    def enqueue(self, new_element):
        # pass
        # new_element.next = self.head
        queue.append(new_element)

        


    def peek(self):
        # pass 
        if not self.empty():
            return self.head
        return None

    def dequeue(self):
        # pass
        queue.pop(0)