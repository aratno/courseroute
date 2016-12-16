'''
graph:
    Helper functions for turning data files (as JSON) into graph structures.

author: Abe Ratnofsky
'''

import os
import json
import pprint

def data_exists():
    '''
    Grabs the last modified data file relative path if it exists, otherwise
    returns False.
    '''
    data_dir = 'data/'
    data_files = os.listdir(data_dir)
    if not data_files:
        return False
    # use last modified data
    data_files = list(map(lambda m: data_dir+m, data_files))    # prepend dir name
    data_files.sort(key=lambda path: os.path.getmtime(path))
    return data_files[-1]

def parse_json(path):
    '''
    Parses JSON into a dict, prunes out unnecessary keys, and generates a graph.
    '''
    with open(path) as f:
        dump = json.load(f)
        code_to_prereqs = {}
        # take course code and prerequisites only
        for k, v in dump.items():
            code_to_prereqs[v['code']] = v['prerequisite']

        pprint.pprint(code_to_prereqs)

def parse_prereqs(prereq_str):
    '''
    Course prerequisites are expressed as semi-structured human-readable
    explanations, and require translation into more formal predicates.

    Here are some examples of prerequisite explanations, from the calendar:
        'CSC209H1, CSC258H1, CSC263H1/CSC265H1, STA247H1/STA255H1/STA257H1/ECO227Y1'
        'STA247H1/STA255H1/STA257H1 or familiarity with basic probability
            theory, including Bayes's theorem; CSC207H1/CSC209H1 or
            proficiency in Python and software development.'
        'Permission of the instructor'
        'Any half-course on computing'
    '''

    pass

if __name__ == '__main__':
    datapath = data_exists()
    if datapath:
        print('Data found at {}'.format(datapath))
    else:
        print('No data available')
        exit(1)
    
    parse_json(datapath)

