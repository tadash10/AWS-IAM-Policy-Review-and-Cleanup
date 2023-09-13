import boto3

def calculate_policy_risk_score(policy):
    # Implement logic to calculate a risk score for the policy
    # Example: Assign higher risk scores to overly permissive policies
    risk_score = 0

    for statement in policy['DefaultVersion']['Document']['Statement']:
        if '*' in statement.get('Action', []):
            risk_score += 10  # Example: Assign 10 risk points for wildcard actions

    return risk_score

if __name__ == "__main__":
    # For testing, provide a policy to calculate the risk score
    policy_to_score = {}  # Replace with an actual policy
    risk_score = calculate_policy_risk_score(policy_to_score)
    print(f"Risk Score for Policy: {risk_score}")
