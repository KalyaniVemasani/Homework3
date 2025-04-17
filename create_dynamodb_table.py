import boto3

def create_dynamodb_table(table_name):
    dynamodb = boto3.client('dynamodb')

    try:
        print(f"\nCreating DynamoDB table: {table_name}")
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        waiter = dynamodb.get_waiter('table_exists')
        waiter.wait(TableName=table_name)
        print(f"Table {table_name} created successfully!")
    except dynamodb.exceptions.ResourceInUseException:
        print(f"Table {table_name} already exists.")

if __name__ == "__main__":
    table_name = 'MyTestTable'
    create_dynamodb_table(table_name)
