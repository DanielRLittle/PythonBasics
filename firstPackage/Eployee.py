

class Employee:
    
    def __init__(self, fName, lName, pay):
        self.fName = fName;
        self.lName = lName;
        self.pay = pay;
        self.email = fName + '.' + lName + '@Company.com';

    def fullName(self):
        return '{} {}'.format(self.fName, self.lName);
    
    def fullName2(self):
        return self.fName, self.lName;

emp_1 = Employee('Danny', 'Li', 23500);

print(emp_1);

print(emp_1.email);

print (emp_1.fullName());

print (emp_1.fullName2());