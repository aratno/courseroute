'''
parse:
    Utility functions for parsing calendar data. Currently, the main use is
    parsing course prerequisites (as strings) into predicates.
author: Abe Ratnofsky
'''

import re
import pprint   # debug

'''
Examples:
CSC148H1 : CSC108H1/(equivalent programming experience)
CSC207H1 : 60% or higher in CSC148H1/CSC150H1
CSC209H1 : CSC207H1
CSC236H1 : 60% or higher in CSC148H1/CSC150H1, 60% or higher in CSC165H1
CSC258H1 : 60% or higher in CSC148H1/CSC150H1, 60% or higher in CSC165H1/CSC240H1
CSC263H1 : CSC207H1, CSC236H1/CSC240H1; STA247H1/STA255H1/STA257H1
CSC265H1 : CSC240H1 or an A- in CSC236H1
CSC300H1 : Any half-course on computing
CSC301H1 : CSC209H1, CSC263H1/CSC265H1
CSC302H1 : CSC301H1
CSC304H1 : STA247H1/STA255H1/STA257H1/PSY201H1/ECO227Y1, (MAT135H1, MAT136H1)/MAT137Y1/MAT157Y1
CSC309H1 : CSC209H1
CSC318H1 : Any CSC half-course
CSC320H1 : CSC209H1/(CSC207H1, proficiency in C or C++); MAT221H1/MAT223H1/MAT240H1, (MAT136H1 with a minimum mark of 77)/(MAT137Y1 with a minimum mark of 73)/(MAT157Y1 with a minimum mark of 67)/MAT235Y1/MAT237Y1/MAT257Y1
CSC321H1 : (MAT136H1 with a minimum mark of 77)/(MAT137Y1 with a minimum mark of 73)/(MAT157Y1 with a minimum mark of 67)/MAT235Y1/MAT237Y1/MAT257Y1, MAT221H1/MAT223H1/MAT240H1; STA247H1/STA255H1/STA257H1
CSC324H1 : CSC263H1/CSC265H1
CSC336H1 : CSC148H1/CSC150H1; MAT133Y1(70%)/(MAT135H1, MAT136H1)/MAT135Y1/MAT137Y1/MAT157Y1, MAT221H1/MAT223H1/MAT240H1
CSC343H1 : CSC165H1/CSC240H1/(MAT135H1, MAT136H1)/MAT135Y1/MAT137Y1/MAT157Y1; CSC207H1.
    Prerequisite for Engineering students only: ECE345H1/CSC190H1/CSC192H1
CSC343H1 : CSC165H1/CSC240H1/(MAT135H1, MAT136H1)/MAT135Y1/MAT137Y1/MAT157Y1; CSC207H1.
    Prerequisite for Engineering students only: ECE345H1/CSC190H1/CSC192H1
CSC358H1 : CSC209H1, CSC258H1, CSC263H1/CSC265H1, STA247H1/STA255H1/STA257H1/ECO227Y1
CSC369H1 : CSC209H1, CSC258H1
CSC373H1 : CSC263H1/CSC265H1
CSC384H1 : CSC263H1/CSC265H1, STA247H1/STA255H1/STA257H1
CSC385H1 : CSC258H1; CSC209H1/proficiency in C
CSC401H1 : CSC207H1/CSC209H1; STA247H1/STA255H1/STA257H1
CSC404H1 : CSC301H1/CSC318H1/CSC384H1/CSC418H1
CSC410H1 : CSC207H1, CSC236H1/CSC240H1
CSC411H1 : CSC263H1/CSC265H1, MAT(135H1,136H1)/MAT137Y1/MAT137Y1/MAT157Y1, STA247H1/STA255H1/STA257H1
CSC412H1 : CSC411H1
CSC418H1 : CSC336H1/CSC350H1/CSC351H1/CSC363H1/CSC365H1/CSC373H1/CSC375H1/CSC463H1, (MAT135H1, MAT136H1)/MAT135Y1/MAT137Y1/MAT157Y1, CSC209H1/proficiency in C or C++;
    &nbsp;Prerequisite for Engineering students only:  ECE345H1 or ECE352H1
CSC420H1 : CSC263H1/CSC265H1, (MAT135H1, MAT136H1)/MAT135Y1/MAT137Y1/MAT157Y1, MAT221H1/MAT223H1/MAT240H1
CSC428H1 : CSC318H1; STA247H1/STA255H1/STA257H1,(STA248H1/STA250H1/STA261H1)/(PSY201H1, PSY202H1)/(SOC202H1, SOC300H1); CSC209H1/proficiency C++ or Java
CSC436H1 : CSC336H1/CSC350H1
CSC438H1 : (CSC363H1/CSC463H1)/CSC365H1/CSC373H1/CSC375H1/MAT247H1
CSC443H1 : CSC343H1, CSC369H1, CSC373H1/CSC375H1
CSC446H1 : CSC351H1/(CSC336H1 (75%))/equivalent mathematical background; MAT237Y1/MAT257Y1; APM346H1/APM351Y1/(MAT244H1/MAT267H1 and exposure to PDEs)
CSC448H1 : CSC236H1/CSC240H1
CSC454H1 : Five CSC half-courses at the 200-level or higher
CSC458H1 : CSC209H1, CSC258H1, CSC263H1/CSC265H1, STA247H1/STA255H1/STA257H1/ECO227Y1
CSC463H1 : CSC236H1/CSC240H1
CSC465H1 : CSC236H1/CSC240H1/MAT309H1
'''

'''
Returns True if the prerequisite description is too complex to naively parse,
otherwise False.
'''
def is_desc_complex(desc):
    desc_cpy = desc[:]
    # Normalize commas and semicolons
    desc_cpy = desc_cpy.replace(';', ',')
    # remove course codes
    desc_cpy = re.sub(r'[A-Z]{3}[0-9]{3}[HY]1', '', desc_cpy)
    # remove simple characters
    desc_cpy = re.sub(r'[ /,()]', '', desc_cpy)
    # if more is left, description is complex
    if desc_cpy:
        return True
    return False

'''
Parses prerequisite description strings (as provided by the artsci calendar)
into formal predicates over a courseload.
'''
def naive_description_into_predicate(desc):
    # Check if requirements are complex
    if is_desc_complex(desc):
        return

    # Normalize commas and semicolons
    desc = desc.replace(';', ',')

    # Parenthesize clauses for order of operations
    clauses = list(map(lambda clause: '('+clause+')', desc.split(',')))

    # Replace slash with or
    clauses = list(map(lambda clause: clause.replace('/', ' or '), clauses))

    # Join with and
    predicate = ' and '.join(clauses)

    # Replace course codes with inclusion check code
    def repl(matchobj):
        return '(course_load.has_taken({}))'.format(matchobj.group(0), matchobj.group(1))
    final = re.sub(r'[A-Z]{3}([0-9]{3})[HY]1', repl, predicate)
    print('Computed predicate:', final)

'''
A set of hard-coded prerequiste functions as a placeholder for eventual best
parsing behavior. Currently only supports those described in parse.py docstring.
All returned lambdas represent satisfiability of a course's prerequisites
by operations on a CourseLoad object passed as a parameter.
'''
def get_hard_coded_prereq_predicate(course):
    if course.code == 'CSC148H1':
        return (lambda course_load: course_load.has_taken(code='CSC108H1'))
    elif course.code == 'CSC207H1':
        return (lambda course_load:
                course_load.has_taken(code='CSC148H1') or
                course_load.has_taken(code='CSC150H1'))
    elif course.code == 'CSC209H1':
        return (lambda course_load: course_load.has_taken(code='CSC207H1'))
    elif course.code == 'CSC236H1':
        return (lambda course_load:
                (course_load.has_taken(code='CSC148H1') or
                course_load.has_taken(code='CSC150H1')) and
                course_load.has_taken(code='CSC165H1'))
    elif course.code == 'CSC258H1':
        return (lambda course_load:
                (course_load.has_taken(code='CSC148H1') or
                course_load.has_taken(code='CSC150H1')) and
                (course_load.has_taken(code='CSC165H1') or
                course_load.has_taken(code='CSC240H1')))

if __name__ == '__main__':
    pass
