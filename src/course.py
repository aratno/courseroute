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
        return '<Course code: {}, title: {}>'.format(self.code, self.title)

class CourseLoad:
    def __init__(self, past=None, current=None):
        if not past:
            self.past = set()
        else:
            self.past = past
        if not current:
            self.current = set()
        else:
            self.current = current


    def has_taken(self, course=None, code=None):
        if course:
            return (course in self.past)
        elif code:
            return (code in list(map(lambda course: course.code, self.past)))
        else:
            raise Exception('Parameters do not make sense')

    def is_taking(self):
        return (course in self.current)
