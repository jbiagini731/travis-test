#!/usr/bin/python

import boto3
import botocore
#import sys
import time

s3 = boto3.resource('s3')
test_bucket = 'arcadia-desktop-automation-resources-repo'
test_file   = 'test_file.txt'
tries = 0

while tries < 5:
  try:
    s3.Object(test_bucket, test_file).load()
  except botocore.exceptions.ClientError as e:
    print('Try number: ' + str(tries))
    if e.response['Error']['Code'] == "404":
      print('Object does not exist, yet...')
      tries+=1
      time.sleep(10)
    else:
      print('An unforseen issue has occurred')
      exit(1)
    raise

#print('PID: ' + str(sys.argv[1]))

#if int(sys.argv[1]) > 0:
#  exit(0)
#else:
#  exit(1)
