#!/usr/bin/env python

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value


    @property
    def score(self):
        return self._score


    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value
        

    @property
    def age(self):
        self._age = 2014 - self._birth
        return self._age


    @age.setter
    def age(self,value):
        self._age = value


        



t = Student()
t.score = 11
t.birth = 22
t.age = 22
print t.age
