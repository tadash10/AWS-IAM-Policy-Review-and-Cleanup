import boto3

def check_compliance_with_best_practices(policy):
    # Implement logic to check policy compliance with AWS best practices
    # Example: Check for overly permissive actions

    for statement in policy['DefaultVersion']['Document']['Statement']:
        if '*' in statement.get('Action', []):
            print(f"Policy {policy['PolicyName']} is non-compliant: It contains overly permissive actions")

if __name__ == "__main__":
    # For testing, provide a policy to check compliance
    policy_to_check = {}  # Replace with an actual policy
    check_compliance_with_best_practices(policy_to_check)
