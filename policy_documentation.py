import boto3

def generate_policy_documentation(policy):
    # Generate policy documentation
    try:
        policy_name = policy['PolicyName']
        policy_arn = policy['Arn']

        # Create a documentation file for the policy
        with open(f"{policy_name}_documentation.txt", "w") as doc_file:
            doc_file.write(f"Policy Name: {policy_name}\n")
            doc_file.write(f"Policy ARN: {policy_arn}\n\n")
            
            # Iterate through policy statements and write them to the documentation
            for statement in policy['DefaultVersion']['Document']['Statement']:
                doc_file.write(f"Statement Effect: {statement['Effect']}\n")
                doc_file.write(f"Statement Action: {', '.join(statement['Action'])}\n")
                doc_file.write(f"Statement Resource: {', '.join(statement['Resource'])}\n")
                doc_file.write(f"Statement Condition: {statement.get('Condition', 'None')}\n\n")
                
            print(f"Policy documentation generated for {policy_name} ({policy_arn})")
    except Exception as e:
        print(f"Error generating policy documentation: {e}")

if __name__ == "__main__":
    # For testing, provide a policy to generate documentation
    policy_to_document = {}  # Replace with an actual policy
    generate_policy_documentation(policy_to_document)
