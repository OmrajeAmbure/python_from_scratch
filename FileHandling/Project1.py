import re


class Employee:
    def __init__(self,id,name,email,dob,designation,phoneNumber,address,department,salary):
        self.__id = id;
        self.name = name;
        self.email = email;
        self.dob = dob
        self.__designation = designation;
        self.__phoneNumber = phoneNumber;
        self.address = address;
        self.department = department;
        self.__salary = salary;

    def getName(self):
        return self .name;
    def getEmail(self):
        return self.email
    def getDob(self):
        return self.dob;
    def getDesignation(self):
        return self.__designation;
    def getPhoneNumber(self):
        return self.__phoneNumber;
    def getAddress(self):
        return self.address;
    def getDepartment(self):
        return self.department;
    def getSalary(self):
        return self.__salary;

    def setId(self,id):
        self.__id = id;
    def setName(self,name):
        self.name = name;
    def setEmail(self,email):
        if email ==  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' :
            self.email = email;
        else:
            raise(re.error,"Email not mathced pls try again !");
    def setDob(self,dob):
        self.dob =dob;
    def setDesignation(self,designation):
        self.__designation = designation;
    def setPhoneNumber(self,phoneNumber):
        if phoneNumber <= 0 or phoneNumber>= 1000000000:
            raise (ValueError," Enter valid phone Number");
        self.__phoneNumber = phoneNumber;
    def setAddress(self,address):
        self.address = address;
    def setDepartment(self,department):
        self.department = department;
    def setSalary(self,salary):
        if salary <= 0 or salary >= 10000000:
            raise (ValueError," Invalid Salary Please Emter Valid Salary !");
        else:
            self.__salary = salary;

    def getEmployeeDetails(self):
        print("=======================================================================")
        return f"ID: {self.__id}\nName : {self.name}\nEmail: {self.email}\nDOB: {self.dob}\nAddress: {self.address}\nDepartment: {self.department}"


print("Enter How Many Employees Record want to Store");
n = int(input());


obj1  = Employee(1,"omraje","omrajea@gmail.com","27/05/2005","AIML Intern",8799911512,"Pune","Technical",12000);
print(obj1.getEmployeeDetails());

obj2 =  Employee(2,"raj","raj@gmail.com","07/08/2004","Data Eng Intern",9158165814,"Mumbai","Technical",15000);
print(obj2.getEmployeeDetails());

obj3 =  Employee(3,"vinay","vinay@gmail.com","27/05/2012","MEARN Stack Intern",9080706050,"Kalyan","Technical",10000);
print(obj3.getEmployeeDetails());

