import boto3

ACCESS_KEY = 'AKIAWZF3T2VBXVZR6V53'
SECRET_KEY = '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'

sess = boto3.Session(region_name = 'ap-south-1')
ddb = sess.client('dynamodb', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

def create_table(name):
    try:
        table = ddb.create_table (
            TableName = name,
            KeySchema = [
                {
                    'AttributeName': 'text',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'start',
                    'KeyType': 'RANGE'
                }
                # {
                #     'AttributeName': 'end',
                #     'KeyType': 'RANGE'
                # }
                ],
                AttributeDefinitions = [
                    {
                        'AttributeName': 'text',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName':'start',
                        'AttributeType': 'S'
                    }],
                    ProvisionedThroughput={
                        'ReadCapacityUnits':1,
                        'WriteCapacityUnits':1
                    }
                
            )
        print(table)
    except Exception:
        pass

def put_item(start, end, text, table):
    table = table
    item = {
        'start':{
            'S': start
        },
        'end':{
            'S': end
        },
        'text':{
            'S': text
        }
    }
    try:
        ddb.get_item(
            TableName=table,
            Key={
                'text':{'S': text}
            }
        )
    except Exception:
        ddb.put_item(TableName = table, Item = item)