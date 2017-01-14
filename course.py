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
