import json
import os
import time
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    client = boto3.client('ec2')
    print('## EVENT')
    print(event)
						
    print('Grabbing id for machine... ' + event['detail']['instance-id'])
    eventid = event['detail']['instance-id']
    describe = client.describe_instances(
        Filters=[
            {
                'Name': 'instance-id',
                'Values': [
                    eventid,
                ],
            },
        ],
    )
    try:
        imageid = describe['Reservations'][0]['Instances'][0]['InstanceId']
        volid = describe['Reservations'][0]['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['AttachTime']
        launchtime = describe['Reservations'][0]['Instances'][0]['LaunchTime']
        securitygroup = describe['Reservations'][0]['Instances'][0]['SecurityGroups'][0]['GroupId']
        eventtime = event['time']
        #these can be turned on if you need to troubleshoot ensuring the launch time and volume id is correct
        #print ('Machine launch time is ' + launchtime)
        #print (volid)

    except:
        print('Failed to grab correct timestamp or variables')
        exit(1)
    #Setting event time, launch time, and converting so we can compare days
    eventconvert = str(eventtime)
    launchconvert = str(volid)
    fixlaunchtime = launchconvert.replace('-', '')
    fixeventtime = eventconvert.replace('-', '')
    comparenew = int(fixeventtime[0:8]) - int(fixlaunchtime[0:8])

    try:
        response = client.describe_security_groups(GroupIds=[securitygroup])
        portdig = response['SecurityGroups'][0]['IpPermissions'][0]['ToPort']
        #if resulted attachment time of ebs volume is less than 2 days, the machine is new
        #and we will check the security group
        if comparenew < 2:
            print('Machine life is less than 2 days old, checking security group')
            if portdig == 22:
                openip = (response['SecurityGroups'][0]['IpPermissions'][0]['IpRanges'][0]['CidrIp'])    
                #just a POC, realistically want a way to iterate through the entire list for it
                if '0.0.0.0' in openip:
                    print('Found disallowed rule, shutting down instance')
                    response = client.stop_instances(
                            InstanceIds=[
                                eventid,
                            ],
                        )
                    print('Stopping instance ' + eventid)
        else:
            print('Machine life is more than 2 days old, exiting')      
    except ClientError as ec2errors:
        print(ec2errors)