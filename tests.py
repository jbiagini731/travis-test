#!/usr/bin/python

import argparse
import boto3
import botocore
import time
from decimal import *

parser=argparse.ArgumentParser()

parser.add_argument('--max_duration_in_hours', help='total duration that the test should not exceed')

args=parser.parse_args()

print('Max duration: %s hours' % args.max_duration_in_hours)

# The file polling will occur 5 times in equal intervals starting at the second half of the specified duration
max_attempts = 5
results_file = False
s3           = boto3.resource('s3')
test_bucket  = 'arcadia-desktop-automation-resources-repo'
test_file    = 'test_file.txt'
tries        = 1
sleep_time   = int(Decimal(args.max_duration_in_hours) * 1800)

print('Max attempts: %s' % max_attempts)

# # initial sleep, to be determined - start after half of the total duration has been elapsed
print('Sleeping for half(%s seconds) of the specified duration of %s hours before beginning to check for the results file.' % (sleep_time, args.max_duration_in_hours))
time.sleep(sleep_time)

while tries < max_attempts and not results_file:
  try:
    s3.Object(test_bucket, test_file).load()
    results_file = True
  except Exception as e:
    print('Exception:' + str(e))
    print('Try number: ' + str(tries))
    tries+=1
    time.sleep(sleep_time)

if results_file:
  print('The results file was found.')
else:
  print('The results file was not found.')
  exit(1)
