# Retrieve files from an Amazon S3 Bucket
#
#

import boto3
import botocore
import credentials ## AWS Bucket Credentials
from datetime import date
import os
import shutil
from datetime import datetime
import pandas as pd
from pandas import DataFrame
import gzip
#Gets todays date, puts into a string
today = date.today()
#print("Today's date:", today)
d4 = today.strftime("%Y-%m-%d") #format date to string which will be used as the folder name
last_modified_date = datetime(1939, 9, 1).replace(tzinfo=None)

session = boto3.Session(
    aws_access_key_id=credentials.login['aws_access_key_id'],
    aws_secret_access_key=credentials.login['aws_secret_access_key'],
)

s3 = session.resource('s3')


# Sales
def gets3_st():
    my_bucket = s3.Bucket('<Bucketname>')
    prefix1 = ('<Bucketpath>')
    destination = d4 
    last_modified_date = datetime(1939, 9, 1).replace(tzinfo=None)
    for file in my_bucket.objects.filter(Prefix=prefix1):
         file_date = file.last_modified.replace(tzinfo=None)
    if last_modified_date < file_date:
        last_modified_date = file_date
# you can have more than one file with this date, so you must iterate again
    for file in my_bucket.objects.all():
        path, filename = os.path.split(file.key)
        if file.last_modified.replace(tzinfo=None) == last_modified_date:
        #print(file.key)
        #print(filename)
                if not os.path.exists(d4):
                        os.makedirs(d4) # make the directory
                        my_bucket.download_file(file.key, filename)
                        #shutil.move(filename, destination)
                        shutil.copy(filename, destination)
                        os.remove(filename)
                        print("File name:" + filename)
                else:
                        my_bucket.download_file(file.key, filename)
                        #shutil.move(filename, destination)
                        shutil.copy(filename, destination)
                        os.remove(filename)
                        print("File name:" + filename) #####





#Call the functions
######################################

gets3_st()   




