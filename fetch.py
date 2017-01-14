'''
fetch:
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
Grabs data for all CSC courses. It does not do as much error checking as it
could.  ¯\_(ツ)_/¯
'''
def fetch(url):
    params = {'code':'CSC'}
    print('Fetching URL {}...'.format(url))
    r = requests.get(url, params=params)
    print('URL {} fetched'.format(url))
    output_dir = 'data/'
    f = open(output_dir + 'data-{}.json'.format(time.time()), 'w') 
    f.write(r.text)
    print('File successfully written to ' + output_dir)

if __name__ == '__main__':
    url = 'https://timetable.iit.artsci.utoronto.ca/api/courses'
    fetch(url)
