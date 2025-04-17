import boto3

def list_s3_files(bucket_name):
    s3 = boto3.client('s3')
    print(f"\nListing files in bucket: {bucket_name}")
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f" - {obj['Key']}")
    else:
        print("Bucket is empty or doesn't exist.")

if __name__ == "__main__":
    # Replace with your bucket name
    bucket_name = 'mys3bucketforlab'
    list_s3_files(bucket_name)
