"""n = int(input('enter your number: '))
def pattern(n):
    lastline = n
    lastlinestars = n*4-1
    lastlineoneside = lastlinestars//2

    for i in range(1,n+1):
        if i==1:
            print(' '*lastlineoneside,' * ',' '*lastlineoneside)
        else:
            currentlinestars = i * 4 - 1
            currentlineoneside = currentlinestars // 2
            gapbetweenstars = lastlineoneside - currentlineoneside
            print(' '*gapbetweenstars,'*' * currentlineoneside,' ', '*' * currentlineoneside)

pattern(n)


n = int(input('enter your number: '))
def pattern(n):
    lastline = n
    lastlinestars = n*4-1
    lastlineoneside = lastlinestars // 2

    for i in range(1,n+1):
        if i==1:
            print(' '*lastlineoneside,' * ',' '*lastlineoneside)

        else:
            currentlinestars = i * 4 - 1
            currentlineoneside = currentlinestars // 2
            gapbetweenstars = lastlineoneside - currentlineoneside
            print(' '*gapbetweenstars,'*' * currentlineoneside,' ','*' * currentlineoneside)

pattern(n)


n = int(input('enter your number: '))
def pattern(n):
    lastline = n
    lastlinestars = n * 4 - 1
    lastlineoneside = lastlinestars // 2

    for i in range(1, n + 1):
        if i==1:
            print('*'+'$'*lastlineoneside)

        else:
            currentlinestars = i * 4 - 1
            currentlineoneside = currentlinestars // 2
            gapbetweenstars = lastlineoneside - currentlineoneside
            print(currentlineoneside*'*',gapbetweenstars*'$')

pattern(n)


n = int(input('enter your number: '))
def pattern(n):
    lastline = n
    lastlinestars = n * 4 - 1
    lastlineoneside = lastlinestars // 2

    for i in range(1, n + 1):
        if i==1:
            print(' ' * lastlineoneside, ' * ', ' ' * lastlineoneside)

        else:
            print('*',' ' * lastlineoneside, ' * ', ' ' * lastlineoneside,'*')


pattern(n)

class Airport:
    def __init__(self,name,age):
        self.name = name
        self.age = age


p1 = Airport("John", 36)
print(p1.name)
print(p1.age)

p1 = Airport("adsnan", 36)
print(p1.name)
print(p1.age)

p1 = Airport("hasnain", 36)
print(p1.name)
print(p1.age)

class MyClass:
    def __init__(self,name,terminal):
        self.name = name
        self.terminal = terminal

    def get_details(self):
        return self.name+'@##@@@#'+self.terminal

p1 = MyClass("adnan", "ssdsdf")
print(p1.get_details())

#Homework

n = int(input('enter your number: '))
def pattern(n):
    lastline = n
    lastlinestars = n * 4 - 1
    lastlineoneside = lastlinestars // 2

    for i in range(1, n + 1):
        if i==1:
            print('*'+'$'*lastlineoneside)

        else:
            currentlinestars = i * 4 - 1
            currentlineoneside = currentlinestars // 2
            gapbetweenstars = lastlineoneside - currentlineoneside
            print(currentlineoneside*'*',gapbetweenstars*'$')

pattern(n)

row = int(input('enter your number: '))
for i in range(row):
    print(' '*(row-i)+' *'*(i+1))

for j in range(row):
    print(' '*(j+2)+' *'*(row-1-j))
       


a = [1,1,1,2,2,3,3,3,3,4,4,6,6]

count = {}

for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

output = ",".join(f"({key}={value})" for key, value in count.items())
print(output)

a = [1,7,10,29,34,54,3,2,45,67,54,78]

a.sort()
print(a)

class Building:
    def __init__(self, name, floor, lift):
        self.name = name
        self.floor = floor
        self.lift = lift

    def get_details(self):
        return f"Building Name: {self.name}, Floors: {self.floor}, Lifts: {self.lift}"

my_building = Building("Skyline Tower", 15, 3)

print(my_building.get_details())


# def create_node(data):
#     return {"data": data, "Next": None}
#
#
# def printlist(head):
#     current = head
#
#
# a = create_node(1)
# print(a)
#
# b = create_node(2)
# print(b)

class AiModels():
    def __init__(self, name, context):
        self.name = name
        self.context = context


class Agent(AiModels):
    def __init__(self, name1):
        self.name1 = name1
        super().__init__('agent', 'neuron')

    def hello(self):
        return "hello " + self.name1


p2 = Agent("adnan")
p2.hello()
print(p2.hello())


class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def get_person_details(self):
        return self.name + "" + self.contact


class Student(Person):
    def __init__(self):
        super().__init__("adnan", "5555555")


class Teacher(Person):
    def __init__(self, name, contact):
        super().__init__(name, contact)


p3 = Teacher("zaid", "872378")
print(p3.get_person_details())

p4 = Teacher("subhan", "872378")
print(p4.get_person_details())

p2 = Student()
print(p2.get_person_details())


def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


fibonacci_series(6)

dict1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
         11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
         20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}


def recursion(n):
    if n <= 26:
        print(dict1[n])
        n = n + 1
        return recursion(n)


a = recursion(3)
print(a)

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def recursion(n):
    if n <= 26:
        print(list1[n])
        breakpoint()
        return recursion(n)


a = recursion(8)
print(a)

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def recursion(n, i=0):
    if i < n:
        print(list1[i])
        recursion(n, i + 1)
    else:
        return


num = int(input("Enter a number: "))
recursion(num)

a = [1, 2, 3, 4, 5, 6, 'a', 'b']


def linear_search(n):
    z = -1
    for i in a:
        z = z + 1
        if i == n:
            return z


b = linear_search('a')
print(b)

l1 = [1, 2, 3, 4, 5, 987]


def square(n):
    l2 = []
    for i in n:
        c = i * i
        l2.append(c)
    return l2


a = square(l1)
print(a)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, ]


def add(n):
    total = 0
    for i in n:
        total = total + i
    return total


v = add(l1)
print(v)

#Bubble sort algorithm
l1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def bubble_sort(l1):
    endindex = len(l1)
    for i in range(0, endindex):
        # print(l1[i])
        for j in range(0, endindex - i - 1):
            if l1[j] > l1[j + 1]:
                l1[j], l1[j + 1] = l1[j + 1], l1[j]

    return l1


d = bubble_sort(l1)
print(d)"""

#Merge Sort
# l1 = [3, 4, 55, 2, 5, 9, 43]

l1 = [6,5,4,3,55,44]

def merging(l1,l2):
    i = j = 0
    result = []
    # print(l1,l2)
    for sbc in range(0,len(l1)):
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i = i + 1
        else:
            result.append(l2[j])
            j = j + 1

    result.extend(l1[i:])
    result.extend(l2[j:])
    return result

def merge_sort(l1):
    if len(l1) <= 1:
        return l1
    midpoint = len(l1) // 2

    left1 = merge_sort(l1[:midpoint])
    right1 = merge_sort(l1[midpoint:])
    return merging(left1,right1)

a = merge_sort(l1)
print(a)