### Introduction
The purpose of this is for use with a Lambda that will do the following:
- a cloudwatch event will be set that will look for the initialization of an ec2, this is power on
- upon this cloudwatch event, it will trigger a lambda made with this python code as source
- the python script will then take the information from the ec2 and check the security group
- the security group will be searched for port 22 open to the world.  
- if port 22 is found open to the world instead of internal, it will turn the ec2 instance off

### How it works
- when an ec2 is spun up and fed back to a lambda, the information is given via a json array
- an ec2 itself can't be compared simply by the time it was last on as it could be seen as days, weeks or minutes
- however, when an ec2 is created, the volume id creation date will always stay the same (unless it's swapped)
- the lambda will describe the ec2 instance, look up the volume id, compare the current time vs when it was made
- this determines that if the ec2 is less than 2 days old, it's worth auditing as a newly created ec2 on launch

It should be noted that any of these can be edited of course, you can change the number of days, you can change the delta between them.
You can also change the action instead of stopping the instance to perhaps edit the security group.

The output of the log will be in the cloudwatch group of the lambda you create.  