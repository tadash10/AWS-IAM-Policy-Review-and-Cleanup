import boto3

def list_policies():
    iam_client = boto3.client('iam')

    # List all IAM policies
    response = iam_client.list_policies()
    policies = response['Policies']
    
    return policies

def list_roles():
    iam_client = boto3.client('iam')

    # List all IAM roles
    response = iam_client.list_roles()
    roles = response['Roles']
    
    return roles

def get_attached_roles_and_users(policy_arn):
    iam_client = boto3.client('iam')

    # List IAM roles and users attached to the policy
    response = iam_client.list_entities_for_policy(PolicyArn=policy_arn)
    roles = response['PolicyRoles']
    users = response['PolicyUsers']
    
    return roles, users

def main():
    print("IAM Policy Review and Cleanup Script")

    # List all IAM policies
    policies = list_policies()

    for policy in policies:
        policy_name = policy['PolicyName']
        policy_arn = policy['Arn']

        print(f"Policy: {policy_name} ({policy_arn})")

        # Analyze policy here (e.g., check for overly permissive policies)

        # List IAM roles and users attached to the policy
        roles, users = get_attached_roles_and_users(policy_arn)

        if roles:
            print("Roles attached to this policy:")
            for role in roles:
                print(f" - Role: {role['RoleName']} ({role['Arn']})")

        if users:
            print("Users attached to this policy:")
            for user in users:
                print(f" - User: {user['UserName']} ({user['Arn']})")

        # Implement cleanup logic here if needed

if __name__ == "__main__":
    main()
