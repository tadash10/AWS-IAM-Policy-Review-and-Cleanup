import boto3

def remove_unused_roles(roles):
    # Implement logic to remove unused IAM roles
    for role in roles:
        # Check if the role is unused (you can use the previous code for detection)
        if role_is_unused(role):
            # Remove the unused role
            iam_client = boto3.client('iam')
            try:
                iam_client.delete_role(RoleName=role['RoleName'])
                print(f"Removed unused role: {role['RoleName']}")
            except Exception as e:
                print(f"Error removing role {role['RoleName']}: {e}")

def modify_policy_permissions(policy, new_permissions):
    # Implement logic to modify policy permissions to be more restrictive
    iam_client = boto3.client('iam')

    try:
        # Create a new version of the policy with modified permissions
        response = iam_client.create_policy_version(
            PolicyArn=policy['Arn'],
            PolicyDocument=new_permissions,
            SetAsDefault=True
        )
        print(f"Modified permissions for policy: {policy['PolicyName']} ({policy['Arn']})")
    except Exception as e:
        print(f"Error modifying policy {policy['PolicyName']}: {e}")

if __name__ == "__main__":
    # For testing, provide a list of roles and policies for cleanup and modification
    roles_to_cleanup = []  # Replace with actual roles
    policy_to_modify = {}  # Replace with an actual policy
    new_permissions = {}  # Replace with modified permissions
    remove_unused_roles(roles_to_cleanup)
    modify_policy_permissions(policy_to_modify, new_permissions)
