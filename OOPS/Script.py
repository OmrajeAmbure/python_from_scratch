class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print("woof woof")

class Owner:
    def __init__(self,name,address,contact_number):
        self.name = name;
        self.address = address;
        self.contact_number = contact_number;

owner1 = Owner("om","Dahiwadi",8799911512);
dog1 = Dog("Moti","Rohuni",owner1);
print(f"Dog Name : {dog1.name} Breed is : {dog1.breed} ");
print(f"Dog Owner Info:  {dog1.owner.name} | {dog1.owner.address} | {dog1.owner.contact_number}");
# print(dog1.owner.contact_number)
owner2 = Owner("raj","Pune",9158165814);
dog2 = Dog("Tommay","German Shefard",owner2);
# print(dog2.owner.name);