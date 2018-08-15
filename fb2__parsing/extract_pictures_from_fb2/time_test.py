#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from fb2_pictures__using_lxml import do as do1
from fb2_pictures__using_re import do as do2
from fb2_pictures__using_xml_expat import do as do3


file_name = '../input/Непутевый ученик в школе магии 1. Зачисление в школу (Часть 1).fb2'
count = 10

from timeit import timeit
print('LXML:      {:.3f} secs'.format(timeit('do1(file_name, False)', globals=globals(), number=count)))
print('XML EXPAT: {:.3f} secs'.format(timeit('do3(file_name, False)', globals=globals(), number=count)))
print('RE:        {:.3f} secs'.format(timeit('do2(file_name, False)', globals=globals(), number=count)))
