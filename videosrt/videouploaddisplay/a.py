import boto3
import re

ACCESS_KEY = 'AKIAWZF3T2VBXVZR6V53'
SECRET_KEY = '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'

sess = boto3.Session(region_name = 'ap-south-1')

def look(table, key):
    ddb = sess.resource('dynamodb', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    table = ddb.Table(table)
    response = table.scan()
    items = response['Items']
    newlist = []
    for item in items:
        if(re.search(key, item['text']) != None):
            # i = item['start'] + ' - ' + item['end']
            newlist.append(item)
    return newlist