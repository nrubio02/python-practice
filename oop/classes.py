# Example of class creation
class Customer:
    """ Probando el docstring """

    def set_name(self, new_name):
        self.name = new_name

    def identify(self):
        print("I am Customer ")


cust = Customer()
cust.set_name("Nilson")
cust.identify()


# Examples of constructors, class methods (Java's static methods)
class Employee:
    # Class variables are mostly used for constants
    MIN_SALARY = 3000

    def __init__(self, name, salary=3000):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY

    # Class methods are equivalent to static methods in Java
    @classmethod
    def from_file(cls, name):
        print("Executing class method")
        # Calling the constructor via 'cls' from the class method
        return cls(name)


print("=====")
emp = Employee.from_file("Nilson")
print(emp.name)
print(emp.salary)


# Operator overload
class Customer:
    def __init__(self, cust_id, name, balance):
        self.cust_id, self.name, self.balance = cust_id, name, balance

    def __eq__(self, other):
        print("Calling overloaded equals operator")
        return self.cust_id == other.cust_id and self.name == other.name

    def __str__(self):
        cust_str = """
                    Customer:
                       name: {name}
                       balance: {balance}
                    """.format(name=self.name, balance=self.balance)

        return cust_str

    def __repr__(self):
        """
        By convention, this string should allow to reproduce the object, hence it looking like a constructor call
        """
        return "Customer({cust_id}, '{name}', {balance})".format(cust_id=self.cust_id, name=self.name,
                                                                balance=self.balance)


print("=====")
c1 = Customer(123, "Nilson", 1000)
c2 = Customer(123, "Nilson", 1000)
print(c1 == c2)
print(c1)

# Operator overload applies to:
#   !=      __ne__
#   >=      __ge__
#   <=      __le__
#   >      __gt__
#   <      __lt__

# In case of comparing a child class to its super class, Python will use the child's operator method to compare
