#single inheritance
# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()
d.speak()
d.bark()


#multiple inheritance


class Father:
    def skill(self):
        print("father knows everything")


class Mother:
    def work(self):
        print("mother knows cooking")


class child(Father, Mother):
    def hobby(self):
        print("child love both")


a = child()
a.skill()
a.work()
a.hobby()


#Hierarchical inheritance
class Animal:
    def speak(self):
        print("animal speaks")


class Dog(Animal):
    def bark(self):
        print("dog barks")


d = Dog()
d.speak()
d.bark()


class Cat(Animal):
    def meaow(self):
        print("cat meaow")


c = Cat()
c.speak()
c.meaow()