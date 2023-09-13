import boto3

def detect_unused_resources(roles, users):
    cloudtrail_client = boto3.client('cloudtrail')

    # Retrieve CloudTrail logs to check for resource usage
    try:
        response = cloudtrail_client.lookup_events(LookupAttributes=[{'AttributeKey': 'ResourceName', 'AttributeValue': 'arn:aws:iam::account-id:role/role-name'}])
        events = response['Events']
    except Exception as e:
        print(f"Error retrieving CloudTrail logs: {e}")
        return

    # Implement logic to detect unused IAM roles and users based on CloudTrail events
    for role in roles:
        role_name = role['RoleName']
        role_arn = role['Arn']
        if not any(event['Username'] == role_name for event in events):
            print(f"Role {role_name} ({role_arn}) is unused.")

    for user in users:
        user_name = user['UserName']
        user_arn = user['Arn']
        if not any(event['Username'] == user_name for event in events):
            print(f"User {user_name} ({user_arn}) is unused.")

if __name__ == "__main__":
    # For testing, provide lists of roles and users to check for unused resources
    roles_to_check = []  # Replace with actual roles
    users_to_check = []  # Replace with actual users
    detect_unused_resources(roles_to_check, users_to_check)
