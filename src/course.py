'''
course:
    Class definitions for courses. For simplicity, time-sensitive data is excluded,
    such as year offered, session code, and meeting times.

author: Abe Ratnofsky
'''

class Course:
    def __init__(self, code, title,  description, prerequisite, corequisite, exclusion):
        self.code = code
        self.title = title
        self.description = description
        self.prerequisite = prerequisite
        self.corequisite = corequisite
        self.exclusion = exclusion

    def __repr__(self):
        return '({}, {})'.format(self.code, self.title)

class CourseLoad:
    def __init__(self, past=None, current=None):
        if not past:
            self.past = set()
        if not current:
            self.current = set()

    def has_taken(self, course):
        return (course in self.past)

    def is_taking(self):
        return (course in self.current)
