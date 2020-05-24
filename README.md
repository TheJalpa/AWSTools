# AWSTools
Miscellaneous AWS Tools that can be used for various use cases

### Categories
- Python
- Terraform

### Python Tools
- EC2 Handler: This tool is used to audit new ec2 instances launched, and will use a lambda to discern if security group rules meet guidelines.  The Lambda will turn an instance off to protect a machine from being thrown into public realms that aren't desirable.  Example: Someone makes an ec2 with ssh open to the world.  The lambda will be invoked by a cloudwatch rule, describe the instance, look at the volume id, compare time stamps, and if a new machine is seen then it will check security group.  If rule == Desired ruleset, turn off machine, else leave it alone.

### Terraform
- ec2creation: This is a very quick and easy terraform plan that's been var'd out for you.  Fill out the vars, execute terraform, and spin up an EC2.