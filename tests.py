#!/usr/bin/python

import sys

print('PID: ' + str(sys.argv[1]))

if str(sys.argv[1]) > 0:
  exit 0
else:
  exit 1
