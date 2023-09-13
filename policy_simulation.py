import boto3

def simulate_policy_effect(policy, resource):
    iam_client = boto3.client('iam')

    # Simulate policy effect
    try:
        response = iam_client.simulate_principal_policy(
            PolicySourceArn=policy['Arn'],
            ActionNames=['ActionToSimulate'],
            ResourceArns=[resource['Arn']],
        )

        # Check if the simulation allows the specified action
        if any(effect['EvalDecision'] == 'allowed' for effect in response['EvaluationResults']):
            print(f"The policy allows the action on resource: {resource['Arn']}")
        else:
            print(f"The policy denies the action on resource: {resource['Arn']}")
    except Exception as e:
        print(f"Error simulating policy effect: {e}")

if __name__ == "__main__":
    # For testing, provide a policy and resource to simulate
    policy_to_simulate = {}  # Replace with an actual policy
    resource_to_simulate = {}  # Replace with an actual resource
    simulate_policy_effect(policy_to_simulate, resource_to_simulate)
