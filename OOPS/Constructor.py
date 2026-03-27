class Constructor:
    def __init__(self):
            self.__name = "";
    def getName(self):
            return self.__name
    def setName(self,name):
            self.__name = name;
obj1 =  Constructor();
obj2 = Constructor();
obj1.setName("om");
print(obj1.getName());

print(id(obj1)) # Show the Address of object in Heap Memory --> ex. 2607402857008
print(id(obj2)) #

print(obj1._Constructor__name);
print(Constructor.__dict__)