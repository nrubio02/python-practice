class Example:

    # Attributes that should be treated as internal should be prefixed with a single underscore
    # i.e Don't touch this attribute!
    # Attributes with leading double underscore means they're pseudo private methods. These are interpreted
    # in a special way by Python
    def __init__(self):
        self._internal = None
        self.__pseudo_private = None

    def _internal_method(self):
        """ This is an internal method """
        pass

    def __private_method(self):
        """ This is a pseudo private method """
        pass


# Defining properties
class Employee:
    def __init__(self, name, new_salary):
        self._salary = new_salary

    # Defining the 'getter' for the property
    @property
    def salary(self):
        return self._salary

    # Defining the 'setter' for the property
    @salary.setter
    def salary(self, new_salary):
        """ Add validations and set the new salary """
        if new_salary < 0:
            raise ValueError("Invalid salary!")
        self._salary = new_salary


emp = Employee("Nilson", 1000)
emp.salary
emp.salary = 2000
emp.salary
