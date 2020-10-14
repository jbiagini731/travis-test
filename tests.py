#!/usr/bin/python

import boto3
import botocore
import time

s3 = boto3.resource('s3')
test_bucket = 'arcadia-desktop-automation-resources-repo'
test_file   = 'test_file.txt'
tries = 0
results_file = False
while tries < 3 and not results_file:
  try:
    s3.Object(test_bucket, test_file).load()
    results_file = True
  except Exception as e:
    print('Exception:' + str(e))
    print('Try number: ' + str(tries))
    tries+=1
    time.sleep(10)

if not results_file:
  exit(1)
