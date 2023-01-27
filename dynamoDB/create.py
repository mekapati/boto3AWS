import boto3 

dynamodb = boto3.resource('dynamodb') 

table = dynamodb.create_table ( 
    TableName = 'users',
    KeySchema = [
        {
            'AttributeName': 'username', 
            'KeyType': 'HASH'
        },
        {
            'AttributeName' : 'last_name',
            'KeyType': 'RANGE'
        }
    ], 
    AttributeDefinitions = [
        {
            'AttributeName' : 'username',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'last_name',
            'AttributeType' : 'S'
        }, 
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits' : 5,
        'WriteCapacityUnits' : 5
    }
) 
# wait until the tabel exists
table.meta.client.get_waiter('table_exists').wait(TableName = 'users') 

# print(table.item_count)  

table = dynamodb.Table('users')
 
table.put_item(
    Item = {
        'username' : 'mekapatimalyadri',
        'first_name' : 'mekapati',
        'last_name' : 'malyadri',
        'age' : 25,
        'account_type' : 'standard_user',
    }
 )