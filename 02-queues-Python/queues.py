"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]
        # self.storage = [tail]
        # queue=[]

    def enqueue(self, new_element):
        # pass
        # new_element.next = self.head
        self.storage.append(new_element)

        


    def peek(self):
        # pass 
        # if not self.empty():
        #     return self.head
        # return None
        return self.storage[0]

    def dequeue(self):
        # pass
        deq=self.storage.pop(0)
        return deq