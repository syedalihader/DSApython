'''def welcome():
    print("Introduction to function")
welcome()

def name():
    name= input("Enter your Name:")
    print(name,"Welcome to Python 101")
name() 

def add():
    num1=int( input('num 1 is:'))
    num2=int( input('num 1 is:'))
    sum = num1+num2
    print("sum of number is",sum)
    add()
def product():
    num1=int( input('num 1 is:'))
    num2=int( input('num 2 is:'))
    result = num1*num2
    print("Product of two numbers is:", result)
product()

def difference():
    num1=int( input('num 1 is:'))
    num2=int( input('num 2 is:'))
    result = num1-num2
    print("Difference of two numbers is:", result)
difference()
  
  
def animals(a,b,c):
      animalG={"koyal":a,"dog":b,"cat":c}
      return animalG   
output = animals("koyal","dog","cat") 
print(output) 


def palindromeCheck(num):
    temp = num
    rev = 0
    while (num != 0):
        r = num % 10
        rev = rev * 10 + r
        num = num // 10
    if (rev == temp):
        print(temp, "is a palindrome number")
    else:
        print(temp, "is not a palindrome number")

''mypoem=(Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference.)
print(mypoem)

def school(a,b,c,d):students=("ali":a, "haider":b, "kambo")'''
class stack():
   def __init__(self):
       self.items = []  
       
   def push(self,item):
      self.items.append(item)
      return item
   def pop(self):
       return self.items.pop()
   def is_empty(self):
       return self.items ==[]
   def peek(self):
         if not self.is_empty():
              return self.items[-1]
   def get_stack(self):
       return self.items
        
    
mystack  =stack()
print(mystack.push("a"))
print(mystack.push("b"))
print(mystack.push("c"))
print(mystack.push("d"))         
print(mystack.peek())
print(mystack.pop())
            
