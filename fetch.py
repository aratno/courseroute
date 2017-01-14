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
import json
import os
import pprint   # debugging

from course import Course

data_dir = 'data/'

'''
Grabs data for all CSC courses, and writes it to a file. Returns the filepath
written to.
'''
def fetch(url):
    # fetch data
    params = {'code':'CSC'}
    print('Fetching URL {}...'.format(url))
    r = requests.get(url, params=params)
    print('URL {} fetched'.format(url))

    # write to disk
    filepath = data_dir + 'data-{}.json'.format(time.time())
    f = open(filepath, 'w') 
    f.write(r.text)
    print('File successfully written to {}'.format(filepath))
    return filepath

'''
Returns an array of Courses, populated from the fetched JSON.
'''
def parse(filepath):
    f = open(filepath, 'r')
    j = json.load(f)
    v = list(j.values())
    all_courses = set()
    for course_dump in v:
        c = Course(
                course_dump['code'], course_dump['courseTitle'],
                course_dump['courseDescription'], course_dump['prerequisite'],
                course_dump['corequisite'], course_dump['exclusion'])
        all_courses.add(c)
    pprint.pprint(all_courses)
    # TODO: determine format for prerequisite, corequisite, exclusion

if __name__ == '__main__':
    url = 'https://timetable.iit.artsci.utoronto.ca/api/courses'
    # TODO: if data dir empty, fetch, else use first dump; use os.listdir
    data_filepaths = list(map(lambda filename: data_dir+filename, os.listdir(data_dir)))
    if len(data_filepaths) == 0:
        print('No data found, fetching new data')
        fp = fetch(url)
    else:
        fp = data_filepaths[0]
        print('Existing data found, using {}'.format(fp))
    parse(fp)
