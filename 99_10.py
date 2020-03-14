class Person:
    def __init__(self, name):
        self.name = name
    
    def sayHello(self):
        print(f'hi, i am {self.name}')

def demo_class():
    wen = Person('wen')
    wen.sayHello()

    print(type(wen))
    print(isinstance(wen, Person))

def demo_type():
    print(type(1))
    print(isinstance(1,int))
    print(isinstance(1.0,float))
    print(isinstance('1.0',str))
    print(type(int))


def demo_range():
    rangeVar = range(0)
    print(rangeVar)
    print(type(rangeVar))
    print(list(rangeVar))
    listVar = list(rangeVar)
    print(type(listVar))

# 
# demo_type()
demo_class()
exit()


for col in range(9,0,-1):
    for black in range(9-col):
        print('\t',end='')
    for line in range(col,0,-1):
        print(f'{line}*{col}={col*line}\t',end='')
    print()

