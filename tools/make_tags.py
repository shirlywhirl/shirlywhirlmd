#!/mnt/src/shirlywhirlmd/tools/venv/bin/python

import os
import re
from collections import defaultdict

CATEGORICAL_SUBSTR = ['logy',
'obgyn',
'surgery',
'pediatrics',
'peds',
'familymed',
'internalmedicine',
'corona',
'ppe',
'resident',
'intern',
'inpatient',
'outpatient',
'attending',
'medstudent',
'doctor',
'admin',
'nurse',
'black',
'blm',
'singlepayer',
'relatable',
'uchicago',
'pritzker',
'womeninmedicine',
'graphicmedicine',
'premed',
'premedmotivation',
'professionalism',
'pgy',
'ms',
'step',
'shelf',
'opioid',
'ivf',
'mcat',
'uworld']

def main():
    path = '/mnt/src/shirlywhirlmd/_posts/'
    for f in os.listdir(path):
        if not f.endswith('.md'):
            continue
        print("processing: {}".format(f))
        post_path = os.path.join(path, f)
        with open(post_path,  'r') as opost:
            data = opost.readlines()

        tags = set()
        cat = set()

        for line in data:
            for word in re.split('#', line):
                if len(word) > 25 or len(word) <= 2:
                    continue
                if not word.strip().isalnum():
                    continue
                word = word.strip()
                tags.add(word.lower())
                for w in CATEGORICAL_SUBSTR:
                    if w in word:
                        cat.add(word.title())
        tags = tags
        cat = cat

        for index in range(0, len(data)):
            data[index] = re.sub('categories: \[Medicine\]', 'categories: {}'.format(list(cat)), data[index])
            data[index] = re.sub('tags: \[comic\]', 'tags: {}'.format(list(tags)), data[index])
        #data = _process_unit(data,'categories: [Medicine]', 'categories', cat)
        #data = _process_unit(data,'tags: [comic]', 'tags', tags)

        with open(post_path, 'w') as post:
            post.writelines(data)

def _process_unit(lines, old, key, value):
    for data in lines:
        if any(value):
            data.replace(old, '{}: {}'.format(key, value))
        else:
            data.replace(old, '{}: no_{}'.format(key, key))
    return lines

if __name__ == '__main__':
    main()
