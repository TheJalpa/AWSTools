### EC2 Creation in AWS with terraform 12

This terraform plan will allow you to create an EC2 on a very minimal terraform plan.
The vars file exists so that you can add some tags, specify an AMI and spin an EC2 up in no time.
The terraform is very minimal with as little as possible to make this thin with easy documentation.

### How to use

Ensure that your ~/.aws/credentials are updated.  If you do not have an active key for default, you'll need one.
You can do that by installed awscli.  
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

You will then need to configure it
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

Terraform init will download your provider for aws and everything you need.
Terraform plan to review all changes to make sure it's what you want.
Terraform apply to create the ec2.

### What AMI should you use?
Keep in mind that an AMI can change upon updates from time to time.
You can go to your AWS console and then "EC2" and then under images "AMIs" and then can search a specific image.
For instance if you want Ubuntu, you can search that keyword.  If you want CentOS you can search the image you want to use.
Alternatively you may want to create your own image and customize it to make things easier and keep the AMI the same
but charges may apply to that.

Once you have chosen which one you want, take note of the AMI ID, this can be put into vars.

You can also use aws cli to do a describe and filters to look for it, but console may be faster and easier for most users.