#!/usr/bin/python

import boto3
import botocore
import time

s3 = boto3.resource('s3')
test_bucket = 'arcadia-desktop-automation-resources-repo'
test_file   = 'test_file.txt'
tries = 0

while tries < 5:
  try:
    s3.Object(test_bucket, test_file).load()
  except Exception as e:
    print('Exception:' + str(e))
    print('Try number: ' + str(tries))
    tries+=1
    time.sleep(10)
