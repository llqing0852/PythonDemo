#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def __str__(self):
        return 'Student object (name: %s)' % self._name

    __repr__ =__str__

    def __call__(self):
        print('My name is %s' %self._name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    def print_score(self):
        print('%s: %s' % (self._name, self._score))

    def get_grade(self):
        if self._score >= 90:
            return 'A'
        elif self._score >= 60:
            return 'B'
        else:
            return 'C'

if __name__=='__main__':
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)

    print('bart.name =', bart.name)
    print('bart.score =', bart.score)
    bart.print_score()

    print('grade of Bart:', bart.get_grade())
    print('grade of Lisa:', lisa.get_grade())