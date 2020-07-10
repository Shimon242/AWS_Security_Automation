# Function to stop EC2 instances nightly

import boto3


def lambda_handler(event, context):
    
    # Get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]
               
    
    # Iterative over each region
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        
        print('Region:', region)
        
        #Get running instances only
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['Running']}])
            
        # Stop the instances and print the name for cloudwatch logs
        for instance in instances:
            instance.stop()
            print('Stopped Instances: ', instance.id)

# Change default timeout to at least 1 minute

# Can be set to trigger using cloudwatch event rules eg cron expression 0 23 ? * MON-FRI * for monday to friday at 11pm
