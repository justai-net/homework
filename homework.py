#!/usr/bin/env python2.7
from treeset import TreeSet


class Employee():
    """Details of Employees. Employees contain the following properties:

    Attributes:
    firstName: First name of employee
    lastName: Last name of employee
    age: Age of employee
    """

    def __init__(self, firstName, lastName, age):
        """Returns Employee details"""
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __str__(self):
        return self.age


Takeo = Employee('Takeo', 'Ischi', 70)
Franzl = Employee('Franzl', 'Lang', 85)
Adam = Employee('Adam', 'Inthapanya', 20)


def lastName(arg='lastName'):  # TreeSet Lastname
    if arg == 'lastName':
        print('Sorted by Last Name')
        value = TreeSet([Takeo.lastName, Franzl.lastName, Adam.lastName])
        for i in value:
            print(i)


def sortage(arg='age'):  # TreeSet age
    if arg == 'age':
        print('Sorted by Age')
        value = TreeSet([Takeo.age, Franzl.age, Adam.age])
        for i in value:
            print(i)


if __name__ == "__main__":
    lastName()  # TreeSet Lastname
    sortage()  # TreeSet age
