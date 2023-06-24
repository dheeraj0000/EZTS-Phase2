#stack is LIFO-LAST IN FIRST OUT

stack=[]
def push():
    element=int(input("enter the elements"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("Removed element",e)
        print(stack)
def display():
    if not stack:
        print("stack is empty")
    else:
        print(stack)
def display_even_numbers():
    even_numbers = []
    #odd_numbers=[]
    for number in stack:
        if number % 2 == 0:
            even_numbers.append(number)
        #else:
            #odd_numbers.append(number)
    if even_numbers:
        print("Even numbers in the stack:", even_numbers)
    #elif odd_numbers:
        #print("odd numbers",odd_numbers)
    else:
        print('None')


def display_odd_number():
    odd_numbers=[]
    for number in stack:
        if number%2!=0:
            odd_numbers.append(number)
    if odd_numbers:
        print("odd number in the stack;",odd_numbers)
    else:
        print("no odd numbers there in stack")


def peak():
    print(stack(len(stack)-1))


    
while True:
    print("select operation 1.push 2.pop 3.display 4.peak  5.display_even_numbers 6display_odd_number.7.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        peak()
    elif choice==5:
        display_even_numbers()
    elif choice==6:
        display_odd_number()
    elif choice==6:
        break
    else:
        print("enter the correct operation")
        
        
        
        
        
        
        
        
        '''
    
class singlelinkedlist1:
    def __init__(self):
        self.head=None
        
    def insert_position1(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next

        np.next=temp.next
        temp.next=np
'''
        
