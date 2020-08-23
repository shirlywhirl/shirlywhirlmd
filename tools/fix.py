#!/usr/bin/python

import os

def main():
    for post in os.listdir(os.getcwd()):
        if 'needs-title' in post:
            date = post[0:10]
            with open(post,'r') as f:
                new_post_name = date+ "-" + date + ".md"
                with open(new_post_name, 'w') as p:
                    for line in f.readlines():
                        if "Needs-title" not in line:
                            p.write(line)
                        else:
                            p.write('title: {}\n'.format(date))


if __name__ == '__main__':
    main()
