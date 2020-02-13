#!/usr/bin/env python
import preprocessing
mysql = {'host': 'localhost',
         'user': '<your user>',
         'passwd': '<your password>',
         'db': '<your db name'}
preprocessing_queue = [preprocessing.scale_and_center,
                       preprocessing.dot_reduction,
                       preprocessing.connect_lines]
use_anonymous = True