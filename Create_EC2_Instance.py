# Creates an EC2 instance on Amazon Web Services using a lambda function (using free tier)

import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)


# Use environment variables on lambda to set the EC2 variables
# AMI	ami-09d95fab7fff3776c (free ami)
#INSTANCE_TYPE	t2.micro (free instance type)
#KEY_NAME	(Your create key pair name)
#SUBNET_ID	(Your subnet's ID name)


# In addition to this code you will need a IAM policy that allows lambda access to create an ec2 instance, an example template can be found here https://raw.githubusercontent.com/linuxacademy/content-lambda-boto3/master/Lab-Create-an-EC2-Instance-Using-Lambda/lambda_execution_role.json
