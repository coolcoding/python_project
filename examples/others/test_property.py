#!/usr/bin/env python

class Student():


    @property
    def age(self):
        return self.age


    @age.setter
    def age(self,value):
        self.age = value



s = Student()
print s.age
