#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re


def trans_grade(grades):
    if re.search('高', grades):
        xuebu = '高中'
    elif re.search('七|八|九', grades):
        xuebu = '初中'
    elif re.search('一|二|三|四|五|六', grades):
        xuebu = '小学'
    else:
        xuebu = '其他'
    new_grade = list(set(grades.split(',')))
    new_grade.sort()
    new_grade = ','.join(new_grade)
    return xuebu, new_grade

def process():
    """TODO: Docstring for process.
    """
    while 1:
        line = sys.stdin.readline()
        if len(line)==0:
            break
        try:
            items = line.strip('\n').replace('\x01', '\t').split('\t')
            course_id = items[0]
            course_type = items[1]
            grades = items[2]
            xuebu, new_grade = trans_grade(grades)
            outlist = [course_id, course_type, grades, xuebu, new_grade]
            outstr = '\t'.join('{}'.format(item) for item in outlist)
            # outstr = '\t'.join(items)
            sys.stdout.write('{}\n'.format(outstr))
        except Exception as e:
            print(e)
            continue

if __name__ == '__main__':
    process()
