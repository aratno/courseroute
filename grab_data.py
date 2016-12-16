'''
grab_data:
    This file offers some basic functions for downloading local copies of
    course data. This is to keep testing reliable and prevent bloat in the
    repository. All data files are downloaded from the iit.utoronto.ca API
    endpoint to a local data/ directory that is ignored by git.
    Do not commit these files! They will only slow things down.

author: Abe Ratnofsky
'''

import requests
import time
from flask import Flask

'''
This grabs all CSC courses. It does not do as much error checking as it could,
but this is a toy example.     ¯\_(ツ)_/¯
'''
def get_abridged_data():
    url = 'https://timetable.iit.artsci.utoronto.ca/api/courses'
    params = {'code':'CSC', 'section':'F'}
    print('Fetching url...')
    r = requests.get(url, params=params)
    output_dir = 'data/'
    f = open(output_dir + 'abridged_data_dump - '  + str(time.time()) + '.json', 'w') 
    f.write(r.text)
    print('File successfully written to ' + output_dir)

if __name__ == '__main__':
    get_abridged_data()
