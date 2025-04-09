#!/usr/bin/env python3

import jinja2
import os
import csv

if __name__ == '__main__':
    trees = []
    with open('tree_list.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            trees.append(row)

    template = jinja2.Template(open(os.path.join('design', 'latex', 'design.latex.j2')).read())
    with open(os.path.join('design', 'latex', 'design.latex'), 'w') as f:
        f.write(template.render(trees=trees))
