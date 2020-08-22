#!/usr/bin/python

import os

def main():
    all_posts = open('/mnt/src/shirlywhirlmd/all_posts.txt', 'r').readlines()
    for empty_post in os.listdir(os.getcwd()):
        if 'needs-title' in empty_post:
           date = empty_post[0:10]
           for line in all_posts:
               print "looking for" + date
               print "in: " + line
               if date in line:
                   with open(empty_post,'a') as f:
                       f.write(line)

if __name__ == '__main__':
    main()
