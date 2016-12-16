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
        for k in dump:
            code_to_prereqs[dump[k]['code']] = dump[k]['prerequisite']
        pprint.pprint(code_to_prereqs)

if __name__ == '__main__':
    datapath = data_exists()
    if datapath:
        print('Data found at {}'.format(datapath))
    else:
        print('No data available')
        exit(1)
    
    parse_json(datapath)

