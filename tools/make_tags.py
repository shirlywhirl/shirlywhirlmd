#!/mnt/src/shirlywhirlmd/tools/venv/bin/python

import os
import re

def main():
    path = '/mnt/src/shirlywhirlmd/_posts/'
    for f in os.listdir(path):
        if f.endswith('.md'):
            with open(os.path.join(path,f), 'r') as post:
                data = post.read()


            print(f)
            for word in re.split('#', data):
                if len(word) > 25:
                    continue
                print("tag: {}".format(word.strip()))
                if 'logy' in word:
                    print("categorical")



if __name__ == '__main__':
    main()
