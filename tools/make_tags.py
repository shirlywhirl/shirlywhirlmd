#!/mnt/src/shirlywhirlmd/tools/venv/bin/python

import os
import re

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
        if f.endswith('.md'):
            with open(os.path.join(path,f), 'r') as post:
                data = post.read()

            print(f)
            for word in re.split('#', data):
                if len(word) > 25 or len(word) <= 2:
                    continue
		if not word.strip().isalnum():
                    continue
                print("tag: {}".format(word.strip()))
                for w in CATEGORICAL_SUBSTR:
                    if w in word:
                       print("categorical via : {}".format(w))



if __name__ == '__main__':
    main()
