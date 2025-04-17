import boto3

def insert_item(table_name, item_id, name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    print(f"\nInserting item into {table_name}: {{'id': '{item_id}', 'name': '{name}'}}")
    response = table.put_item(
        Item={
            'id': item_id,
            'name': name
        }
    )
    print("✅ Item inserted successfully!")

if __name__ == "__main__":
    table_name = 'MyTestTable'

    # First item
    insert_item(table_name, '101', 'Kalyani')

    # Second item
    insert_item(table_name, '200', 'Puppy')
