import boto3

def send_high_risk_policy_alert(policy_name, risk_score):
    # Implement logic to send alerts for high-risk policies using SNS or other services
    sns_client = boto3.client('sns')
    topic_arn = "arn:aws:sns:us-east-1:123456789012:HighRiskPolicies"

    message = f"High-risk policy detected: {policy_name}, Risk Score: {risk_score}"

    try:
        sns_client.publish(TopicArn=topic_arn, Message=message, Subject="High-Risk Policy Alert")
        print(f"Alert sent for high-risk policy: {policy_name}")
    except Exception as e:
        print(f"Error sending alert for policy {policy_name}: {e}")

if __name__ == "__main__":
    # For testing, provide a policy name and risk score to send an alert
    policy_name_to_alert = "ExamplePolicy"
    risk_score_to_alert = 15  # Replace with an actual risk score
    send_high_risk_policy_alert(policy_name_to_alert, risk_score_to_alert)
