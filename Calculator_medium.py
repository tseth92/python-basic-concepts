"""Calculator Application to understand the basic concepts of Classes, staticmethod, classmethod
and decorators"""


def logging_decorator(incoming_function):
    def inner_function(*args, **kwargs):
        print('Operation called by', args[0].per_name)
        return incoming_function(*args, **kwargs)
    return inner_function


class Calculator:
    """Calculator class to contain the methods for add, multiply, subtract operations"""

    status = False

    def __init__(self, person_name):
        if not self.status:
            raise ValueError("Calculator is not running. Please update status.")
        self.per_name = person_name

    # remove the comments below if you are not using decorator to log details
    @logging_decorator
    def add(self, a, b):
        #self.print_operator_name(self.per_name)
        return a+b

    @logging_decorator
    def subtract(self, a, b):
        #self.print_operator_name(self.per_name)
        return a-b

    @logging_decorator
    def multiply(self, a, b):
        #self.print_operator_name(self.per_name)
        return a*b

    @logging_decorator
    def add3(self, a, b, c):
        # self.print_operator_name(self.per_name)
        return a + b + c

    @staticmethod    
    def print_operator_name(person_name):
        print("Operation called by", person_name)

    @classmethod
    def set_status(cls):
        cls.status = True

    @classmethod
    def reset_status(cls):
        cls.status = False

    @classmethod
    def getStatus(cls):
        return cls.status


if __name__ == '__main__':
    Calculator.set_status()
    # Calculator.reset_status()
    # reset it and run the code, exception will occur and object will not be
    # created, since the status is False, which means Calculator is off.
    print(Calculator.getStatus())
    aron_calculator = Calculator('Aron')
    ben_calculator = Calculator('Ben')
    cathy_calculator = Calculator('Cathy')
    print(aron_calculator.add(5, 6))
    print(aron_calculator.subtract(4, 2))
    print(cathy_calculator.subtract(3, 1))
    print(cathy_calculator.multiply(4, 5))
    print(cathy_calculator.add3(4, 5, 8))
