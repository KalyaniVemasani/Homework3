import boto3

def print_all_items(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    print(f"\n🔍 Fetching items from table: {table_name}")
    try:
        response = table.scan()
        items = response.get('Items', [])
        if not items:
            print("📭 No items found in the table.")
        else:
            print(f"📦 Found {len(items)} items:\n")
            for item in items:
                print(item)
    except Exception as e:
        print("❌ Error reading items:")
        print(e)

if __name__ == "__main__":
    table_name = 'MyTestTable'  # Change if your table name is different
    print_all_items(table_name)
