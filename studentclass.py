#!/usr/bin/python3
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = {}
        self.GPA = 0.0

    def register_for_course(self, course_name, grade):
        self.courses_registered[course_name] = grade

    def calculate_GPA(self):
        if self.courses_registered:
            self.GPA = sum(self.courses_registered.values()) / len(self.courses_registered)
        else:
            self.GPA = 0.0
